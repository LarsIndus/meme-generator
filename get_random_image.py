import random
import os
from PIL import Image

def get_rand_img(spongebob):
    path ="input"
    pics = os.listdir(path)
    if spongebob:
        pics = [item.lower() for item in pics]
        pics = [file for file in pics if "spongebob" in file]
    random_index = random.randrange(0, len(pics))
    image_url = "input/" + pics[random_index]
    try:
        img = Image.open(image_url)
        return img
    except IOError as e:
        print('IOError: {0}'.format(e))
        return None