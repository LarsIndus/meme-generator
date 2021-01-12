import os
import random
from pathlib import Path
from PIL import Image as img
from PIL.Image import Image
from typing import Union, Optional

def get_rand_img(input_dir: Union[Path, str],
                 spongebob: bool = False) -> Optional[Image]:
    pics = os.listdir(input_dir)
    if spongebob:
        pics = [item.lower() for item in pics]
        pics = [file for file in pics if 'spongebob' in file]
    image_path = input_dir / random.choice(pics)
    try:
        rand_img = img.open(image_path)
        return rand_img
    except IOError as e:
        print('IOError: {0}'.format(e))
        return None