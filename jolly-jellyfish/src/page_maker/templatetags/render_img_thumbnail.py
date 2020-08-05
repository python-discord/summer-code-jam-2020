import os
from pathlib import Path

from PIL import Image
from django import template
from django.conf import settings
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

register = template.Library()


try:
    DRIVER_PATH = os.environ['SELENIUM_DRIVER']
except KeyError:
    raise KeyError('SELENIUM_DRIVER system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC.')


OPTIONS = Options()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--window-size={}".format("1920,1080"))
OPTIONS.add_argument("--hide-scrollbars")


@register.simple_tag()
def render_img_thumbnail(request, url_to_render, webpage_obj, example=False):
    """
    todo: documentation
    :return: Path to generated thumbnail image
    """

    # todo: example page thumbnail generation for new themes
    '''if example:
        temp_example = Webpage()
        temp_example.save()
        context = {}
        temp_example.delete()'''

    # To avoid infinite loops as the page calls itself to render,
    # only run the function if url doesn't end with '?rendering=true' (added below)
    rendering_bool = bool(request.GET.get('rendering', ''))

    # i.e. thumbnail is outdated or does not exist yet (thumbnail_edit_date datetime set to 1, 1, 1)
    if webpage_obj.thumbnail_edit_date < webpage_obj.last_edit_date and not rendering_bool:

        base_dir = Path(settings.BASE_DIR)
        media_dir = Path(settings.MEDIA_ROOT)

        url = request.build_absolute_uri(url_to_render) + '?rendering=true'
        # Can't use only the obj's name as this may contain characters not permitted by file system
        image_path = Path('thumbnails') / f'pg-thumb-{str(webpage_obj.id)}.png'
        full_os_path = str(base_dir / media_dir / image_path)

        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=OPTIONS)

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
        img.thumbnail(size=(500, 500))
        img.save(full_os_path)

        webpage_obj.thumbnail = f'{image_path}'
        webpage_obj.thumbnail_edit_date = timezone.now()
        webpage_obj.save()
