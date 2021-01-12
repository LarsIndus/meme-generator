from meme_generator.generator import *
from meme_generator.get_speech import *
from meme_generator.get_random_image import *
from meme_generator.config import input_dir, output_dir

# default values
SPONGEBOB = False
SPEECH = False
FONT = "impact.ttf"
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
        create_meme(txt_top, img, FONT, "top", SPONGEBOB)
        create_meme(txt_bottom, img, FONT, "bottom", SPONGEBOB)
        img.save(output_dir / 'meme.jpg')
        img.show()
    else:
        print("Error: Image or text not valid")

if __name__ == '__main__':
    main()