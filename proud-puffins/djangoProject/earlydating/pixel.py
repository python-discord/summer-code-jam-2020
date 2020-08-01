from pathlib import Path
from PIL import Image
import os


def pixelate(name):

    # Open File
    absolute = Path.cwd().resolve().parent.parent.joinpath('images', 'users_large')
    img = Image.open(absolute.joinpath(name))

    # Resize smoothly down to 48x48 pixels
    imgSmall = img.resize((48, 48), resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size, Image.NEAREST)

    # Save
    result.save(Path.cwd().resolve().parent.parent.joinpath('images', 'user_pixel', name))


directory = Path.cwd().resolve().parent.parent.joinpath('images', 'users_large')


for filename in os.listdir(directory):
    pixelate(filename)
