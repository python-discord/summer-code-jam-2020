import os
from pathlib import Path
from typing import Union

from PIL import Image
from django import template
from django.conf import settings
from django.http import HttpRequest
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions

from ..models import Webpage, Template

register = template.Library()  # registers function in this file as template tags for use within Django templates


try:
    DRIVER_PATH = os.environ['SELENIUM_DRIVER']
except KeyError:
    raise KeyError('SELENIUM_DRIVER system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC.')


def add_options(
        options_object: Union[ChromeOptions, FireOptions], window_size: str) -> Union[ChromeOptions, FireOptions]:
    """
    Used to quickly add options to options_object - since these are shared by both ChromeOptions & FireOptions
    :param options_object: Options object imported from selenium.webdriver.BROWSER.options
    :param window_size: string in format 'height, width'
    :return Options object with common arguments added
    """
    options_object.add_argument('--headless')
    options_object.add_argument('--hide-scrollbars')
    options_object.add_argument(f'--window-size={window_size}')
    return options_object


@register.simple_tag()
def render_thumbnail(request: HttpRequest, url_to_render: str, page_obj: Union[Webpage, Template]) -> None:
    """
    This function needs to be called from within django html templates using:
        {% load render_thumbnail %}

        {% render_thumbnail request url_to_render page_obj as none %}

    It saves a thumbnail/screenshot of the page from within which it is called to page_obj's thumbnail attribute.
    This is accomplished using a selenium browser driver running in a headless configuration.

    Since, when running a local server, this results in the server being pinged twice (once within itself),
    a ConnectionResetError may be output to the console.
    This is safe to ignore (but can't be escaped, with except, for some reason).

    :param request: A Django HttpRequest object, sourced from the page which is calling this function.
        This is needed in order to access additional GET info and to build a full url (including domain).
    :param url_to_render: The relative url of the webpage to render (e.g. '/pages/page_name').
        Accessed within a template using something like:
        {% url 'webpage-view' pagename=webpage.name as url_to_render %}.
        Also needed to build full url.
    :param page_obj: Either a 'Webpage' or 'Template' Django object. Accessed in order to save thumbnail path.
    """

    is_template = isinstance(page_obj, Template)  # True if object is an instance of models.Template

    is_outdated = False
    if not is_template:
        # only Webpages have the thumbnail_edit_date attr (since they can be edited by the user)
        # True if the thumbnail is outdated or does not exist yet (thumbnail_edit_date datetime set to 1, 1, 1)
        is_outdated = page_obj.thumbnail_edit_date < page_obj.last_edit_date

    if is_template:
        # str(page_obj.thumbnail) returns rel path to thumbnail in str form (not comparable otherwise)
        if 'placeholder_img.png' not in str(page_obj.thumbnail):  # checks if the template actually needs a thumbnail
            is_template = False

    # To avoid infinite loops as the page calls itself to render,
    # ensures function only runs if url doesn't end with '?rendering=true' (added below)
    is_rendering = bool(request.GET.get('rendering', ''))

    if (is_template or is_outdated) and not is_rendering:  # if a thumbnail is needed
        base_dir = Path(settings.BASE_DIR)
        media_dir = Path(settings.MEDIA_ROOT)
        # 'template_' prefix for Template Objects; 'pg_' for Webpages.
        image_prefix = 'template_' if is_template else 'pg_'
        # Can't use only the obj's name as this may contain characters not permitted by file system
        image_path = Path('thumbnails') / f'{image_prefix}thumb-{page_obj.id}.png'
        full_os_path = str(base_dir / media_dir / image_path)

        if is_template:
            window_size = '500,500'  # thumbnails for Templates, due to less content, can be much smaller
        else:
            window_size = '1980,1080'

        if 'chromedriver' in DRIVER_PATH:
            options = add_options(ChromeOptions(), window_size)
            driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        elif 'geckodriver' in DRIVER_PATH:
            options = add_options(FireOptions(), window_size)
            driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
        else:
            raise Exception('The driver specified in SELENIUM_DRIVER is not supported.\n'
                            "Currently, only Chrome/Chromium ('chromedriver') and "
                            "Firefox ('geckodriver') are supported.\n"
                            'Please install one of these browsers and the associated driver.')

        url = request.build_absolute_uri(url_to_render) + '?rendering=true'

        # NB: This function raises: "ConnectionResetError: [WinError 10054] ...
        # An existing connection was forcibly closed by the remote host" in console.
        # This has no functional effect on the program and
        # is likely just a side-effect of the server being pinged from within itself essentially.
        #
        # Celery (for asynchronous tasks) no longer supports Windows - same with Redis.
        # This means that, in this current dev environment where there are multiple OSs at play,
        # having a functioning webpage, while this function executes in the background,
        # doesn't seem possible 😭  TODO: possible using Docker?
        driver.get(url)
        driver.save_screenshot(full_os_path)
        driver.close()

        img = Image.open(full_os_path)
        # image shrunk (aspect ration maintained) to reduce storage space and reduce footprint used on actual webpage
        img.thumbnail(size=(500, 500))
        img.save(full_os_path)

        page_obj.thumbnail = f'{image_path}'  # saves relative path to thumbnail to ImageField attribute
        # only Webpage objects can be edited by user so only they have the thumbnail_edit_date attribute
        if not is_template:
            page_obj.thumbnail_edit_date = timezone.now()
        page_obj.save()  # actually commit changes to model database
