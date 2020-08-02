import os

import imgkit
from django.template.loader import render_to_string

CONFIG = imgkit.config(wkhtmltoimage=os.environ['WKHTML_TO_IMAGE'])


def render_img_thumbnail(webpage, css, config=CONFIG):
    """
    todo: documentation
    :return: Path to generated thumbnail image
    """
    page_string = render_to_string(template_name=None, context={})
    output_path = ""  # will need to use django static
    imgkit.from_string(page_string, output_path=output_path, css="", config=config)
    return output_path
