import os

import imgkit
from django.template.loader import render_to_string

try:
    CONFIG = imgkit.config(wkhtmltoimage=os.environ['WKHTML_TO_IMAGE'])
except KeyError:
    raise KeyError('WKHTML_TO_IMAGE system environment variable not found.\n'
                   'Check the README for details on setting it.\n'
                   'If you have already done so and this error persists, try restarting your PC')


def render_img_thumbnail(webpage, css, config=CONFIG):
    """
    todo: documentation
    :return: Path to generated thumbnail image
    """
    page_string = render_to_string(template_name=None, context={})
    output_path = ""  # will need to use django static
    imgkit.from_string(page_string, output_path=output_path, css="", config=config)
    return output_path
