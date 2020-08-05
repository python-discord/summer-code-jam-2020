import os
from pathlib import Path
from typing import Union

from PIL import Image
from django import template
from django.conf import settings
from django.http import HttpRequest
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..models import Webpage, Template

register = template.Library()


try:
    DRIVER_PATH = os.environ['SELENIUM_DRIVER']
except KeyError:
    raise KeyError('SELENIUM_DRIVER system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC.')


OPTIONS = Options()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--hide-scrollbars")


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

    template_obj_bool = hasattr(page_obj, 'style_sheet')  # True if object is an instance of models.Template

    outdated_bool = False
    if not template_obj_bool:  # only Webpages have the thumbnail_edit_date attr (since they can be edited by the user)
        # True if the thumbnail is outdated or does not exist yet (thumbnail_edit_date datetime set to 1, 1, 1)
        outdated_bool = page_obj.thumbnail_edit_date < page_obj.last_edit_date

    if template_obj_bool:
        # str(page_obj.thumbnail) returns rel path to thumbnail in str form (not comparable otherwise)
        if 'placeholder_img.png' not in str(page_obj.thumbnail):  # checks if the template actually needs a thumbnail
            template_obj_bool = False

    # To avoid infinite loops as the page calls itself to render,
    # ensures function only runs if url doesn't end with '?rendering=true' (added below)
    rendering_bool = bool(request.GET.get('rendering', ''))

    if (template_obj_bool or outdated_bool) and not rendering_bool:  # if a thumbnail is needed
        base_dir = Path(settings.BASE_DIR)
        media_dir = Path(settings.MEDIA_ROOT)
        # 'template_' prefix for Template Objects; 'pg_' for Webpages.
        # Can't use only the obj's name as this may contain characters not permitted by file system
        image_path = Path('thumbnails') / f'{"template_" if template_obj_bool else "pg_"}thumb-{str(page_obj.id)}.png'
        full_os_path = str(base_dir / media_dir / image_path)

        if template_obj_bool:
            window_size = '500,500'  # thumbnails for Templates, due to less content, can be much smaller
        else:
            window_size = '1980,1080'
        OPTIONS.add_argument(f'--window-size={window_size}')

        if 'chromedriver' in DRIVER_PATH:
            driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=OPTIONS)
        elif 'geckodriver' in DRIVER_PATH:
            driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=OPTIONS)
        else:
            raise Exception('The driver specified in SELENIUM_DRIVER is not supported.\n'
                            "Currently, only Chrome ('chromedriver') and Firefox ('geckodriver') are supported.\n"
                            'Please install one of these browsers and the associated driver.')

        url = request.build_absolute_uri(url_to_render) + '?rendering=true'

        # NB: This function raises: "ConnectionResetError: [WinError 10054] ...
        # An existing connection was forcibly closed by the remote host" in console."
        # This has no functional effect on the program and
        # is likely just a side-effect of the server being pinged from within itself essentially.
        #
        # Celery (for asynchronous tasks) no longer supports Windows - same with Redis.
        # This means that, in this current dev environment where there are multiple OSs at play,
        # having a functioning webpage, while this function executes in the background,
        # doesn't seem possible 😭
        driver.get(url)
        driver.save_screenshot(full_os_path)
        driver.close()

        img = Image.open(full_os_path)
        img.thumbnail(size=(500, 500))  # image shrunk to reduce storage space and reduce space used on actual website
        img.save(full_os_path)

        page_obj.thumbnail = f'{image_path}'  # saves relative path to thumbnail to ImageField attribute
        if not template_obj_bool:  # only Webpage objects have this thumbnail_edit_date attribute
            page_obj.thumbnail_edit_date = timezone.now()
        page_obj.save()  # actually commit changes to model database
