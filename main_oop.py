from meme_generator.generator import *
from meme_generator.get_speech import *
from meme_generator.get_random_image import *
from meme_generator.config import input_dir, output_dir
from meme_generator.Meme import Meme

# default values
SPONGEBOB = False
SPEECH = False
LANGUAGE = "de-DE"

def main():
    img = get_rand_img(input_dir, SPONGEBOB)
    
    if SPEECH:
        txt_top = get_txt_from_speech(LANGUAGE)
        txt_bottom = get_txt_from_speech(LANGUAGE)
    else:
        txt_top = input("Type top text here: ")
        txt_bottom = input("Type bottom text here: ")
    
    if img is not None and txt_top is not None and txt_bottom is not None:
        meme = Meme(img = img, txt_top = txt_top, txt_bottom = txt_bottom,
                    spongebob = SPONGEBOB)
        meme.img.save(output_dir / 'meme.jpg')
        meme.show_image()
    else:
        print("Error: Image or text not valid")

if __name__ == '__main__':
    main()