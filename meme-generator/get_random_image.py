import random
import os
from PIL import Image
from pathlib import Path

def get_rand_img(spongebob):
    path = Path.cwd().parent / 'input'
    pics = os.listdir(path)
    if spongebob:
        pics = [item.lower() for item in pics]
        pics = [file for file in pics if 'spongebob' in file]
    random_index = random.randrange(0, len(pics))
    image_url = path / pics[random_index]
    try:
        img = Image.open(image_url)
        return img
    except IOError as e:
        print('IOError: {0}'.format(e))
        return None