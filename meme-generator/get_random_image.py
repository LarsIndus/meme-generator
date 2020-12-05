import random
import os
from PIL import Image
from pathlib import Path

def get_rand_img(spongebob):
    input_dir = Path(__file__).parent / '../input'
    pics = os.listdir(input_dir)
    if spongebob:
        pics = [item.lower() for item in pics]
        pics = [file for file in pics if 'spongebob' in file]
    random_index = random.randrange(0, len(pics))
    image_path = input_dir / pics[random_index]
    try:
        img = Image.open(image_path)
        return img
    except IOError as e:
        print('IOError: {0}'.format(e))
        return None