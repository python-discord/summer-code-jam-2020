import os
from pathlib import Path

import imgkit
from django import template
from django.conf import settings

register = template.Library()

try:
    CONFIG = imgkit.config(wkhtmltoimage=os.environ['WKHTML_TO_IMAGE'])
except KeyError:
    raise KeyError('WKHTML_TO_IMAGE system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC.')


@register.simple_tag(name='request_img_gen')
def render_img_thumbnail(url, webpage_obj, example=False):
    """
    todo: documentation
    :return: Path to generated thumbnail image
    """
    base_dir = Path(settings.BASE_DIR)
    media_dir = Path(settings.MEDIA_ROOT)

    # todo: example page thumbnail generation for new themes
    '''if example:
        temp_example = Webpage()
        temp_example.save()
        context = {}
        temp_example.delete()'''

    image_path = Path('thumbnails') / f'{str(webpage_obj)}.png'
    imgkit.from_url(url, output_path=str(base_dir / media_dir / image_path), config=CONFIG)
    # todo: verbosity issues?
    #  'ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host'
    #
    #  'Loading page (1/2)
    #  Rendering (2/2)'
    webpage_obj.thumbnail = f'{image_path}'
    webpage_obj.save()
    # Seem to return None on first call


@register.simple_tag()
def get_dest_url(request, location):
    return request.build_absolute_uri(location)
