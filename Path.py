import os
from config import *


def get_list():
    Images = []
    for ImageP in ImageDir:
        for i in os.listdir(ImageP):
            Image = os.path.join(ImageP, i)
            ext = Image.split('.')[::-1][0].upper()
            if ext in Extension:
                Images.append(Image)

    return
