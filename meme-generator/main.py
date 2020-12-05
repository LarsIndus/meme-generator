from generator import *
from get_speech import *
from get_random_image import *
from pathlib import Path

if __name__ == '__main__':
    
    LANGUAGE = "de-DE"
    FONT = "impact.ttf"
    SPONGEBOB = False
    SPEECH = False
    
    img = get_rand_img(SPONGEBOB)
    
    if SPEECH:
        txt_top = get_txt_from_speech(LANGUAGE)
        txt_bottom = get_txt_from_speech(LANGUAGE)
    else:
        txt_top = input("Type top text here: ")
        txt_bottom = input("Type bottom text here: ")
    
    if img is not None and txt_top is not None and txt_bottom is not None:
        create_meme(txt_top, img, FONT, "top", SPONGEBOB)
        create_meme(txt_bottom, img, FONT, "bottom", SPONGEBOB)
        output_dir = Path(__file__).parent / '../output'
        img.save(output_dir / 'meme.jpg')
        img.show()
    else:
        print("Error: Image or text not valid")