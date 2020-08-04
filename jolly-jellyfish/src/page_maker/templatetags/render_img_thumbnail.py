import os
from pathlib import Path

import imgkit
from PIL import Image
from django import template
from django.conf import settings
from django.utils import timezone

register = template.Library()

try:
    CONFIG = imgkit.config(wkhtmltoimage=os.environ['WKHTML_TO_IMAGE'])
except KeyError:
    raise KeyError('WKHTML_TO_IMAGE system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC.')


# todo: functionality to regenerate thumbnail if page has changed
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
    if webpage_obj.thumbnail_edit_date < webpage_obj.last_edit_date and not rendering_bool:
        # i.e. thumbnail is outdated or does not exist yet (datetime set to 1, 1, 1)

        base_dir = Path(settings.BASE_DIR)
        media_dir = Path(settings.MEDIA_ROOT)

        url = request.build_absolute_uri(url_to_render) + '?rendering=true'
        # Can't use only the obj's name as this may contain characters not permitted by file system
        image_path = Path('thumbnails') / f'pg-tb-{str(webpage_obj.id)}.png'
        full_os_path = str(base_dir / media_dir / image_path)

        # Note: this function had exited with 'code 1, due to unknown error' in the past.
        # At the time, this was deduced to be due to an output_path that was too long
        # (i.e. over Windows 10's 256 character file path limit).
        #
        # It also raises: "ConnectionResetError: [WinError 10054] ...
        # An existing connection was forcibly closed by the remote host" in console.
        # This has no functional effect on the program and
        # is likely just a side-effect of the server being pinged from within itself essentially.
        #
        # Celery (for asynchronous tasks) no longer supports Windows - same with Redis.
        # This means that, in this current dev environment where there are multiple OSs at play,
        # having a functioning webpage, while this function executes in the background,
        # doesn't seem possible 😭
        imgkit.from_url(url, output_path=full_os_path, config=CONFIG,
                        options={'quiet': '', 'format': 'png'})

        img = Image.open(full_os_path)
        img.thumbnail(size=(500, 500))
        img.save(full_os_path)

        webpage_obj.thumbnail = f'{image_path}'
        webpage_obj.thumbnail_edit_date = timezone.now()
        webpage_obj.save()
