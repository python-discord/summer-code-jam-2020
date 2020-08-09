from PIL import Image
import os.path
from django.core.exceptions import ValidationError


def resolution_checker(image):
    '''check resolution of uploaded images, reject if too small or too big'''
    im = Image.open(image)
    width, height = im.size
    size_in_bytes = os.stat(image).st_size
    if width < 1200 or height < 800:
        return False
    if size_in_bytes > 2_621_400:
        return False
    return True


def file_size(value):
    '''check file size, this is important because of model field'''
    # file has to be less than 2.5MB, else
    # if gets handled by the TempFileUploader.
    # This code does not work with the TempFileUploader.
    limit = 2621400
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


def image_resizer(image):
    '''image resizer utility to generate thumbnails'''
    # also creates the path to save thumbnails
    size = (480, 480)
    thumbnail_path = os.path.splitext(image)[0] + '_thumbnail'
    with Image.open(image) as im:
        im.thumbnail(size)
        im.save(thumbnail_path, 'PNG')
    return thumbnail_path
