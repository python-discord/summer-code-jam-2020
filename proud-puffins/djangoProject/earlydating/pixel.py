from pathlib import Path
from PIL import Image
import os


def pixelate(filename):

    # Open File
    absolute = Path.cwd().resolve().parent.joinpath('djangoProject', 'static', 'users_large')
    img = Image.open(absolute.joinpath(filename))

    # Resize smoothly down to 48x48 pixels
    imgSmall = img.resize((48, 48), resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size, Image.NEAREST)

    # Save
    result.save(Path.cwd().resolve().parent.joinpath('djangoProject', 'static', 'user_pixel', filename))


directory = Path.cwd().resolve().parent.joinpath('djangoProject', 'static', 'users_large')


for filename in os.listdir(directory):
    pixelate(filename)
