from PIL import Image
import os.path
from django.conf import settings

def resolution_checker(image):
    im = Image.open(image)
    width, height = im.size
    size_in_bytes = os.stat(image).st_size
    if width < 1200 or height < 1000:
        return False
    if size_in_bytes > 3_000_000:
        return False
    return True


def image_resizer(image):
    size = (480, 480)
    thumbnail_path = os.path.splitext(image)[0] + '_thumbnail'
    with Image.open(image) as im:
        im.thumbnail(size)
        im.save(thumbnail_path, 'PNG')
    return thumbnail_path
