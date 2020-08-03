from PIL import Image
from django.core.files import File
from io import BytesIO
import os


def imageTrans(image):
    try:
        _, file_extension = os.path.splitext(image.name)
        file_extension = file_extension.split('.')[-1]

        img = Image.open(image)

        imgSmall = img.resize((img.size[0]//3, img.size[1]//3), resample=Image.BILINEAR)

        result = imgSmall.resize(img.size, Image.NEAREST)

        pixel_io = BytesIO()

        result.save(pixel_io, 'JPEG' if file_extension == 'jpg' else file_extension)

        pixel = File(pixel_io, name=image.name)

        return pixel

    except Exception:
        return image