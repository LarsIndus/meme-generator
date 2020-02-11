# Simple meme generator
# Source: https://blog.lipsumarium.com/caption-memes-in-python/

from PIL import ImageFont, ImageDraw
import random

# --------------------------------------------------------------------------------------
def draw_text(text, draw, font, x, y, offset = 3):
    """Prints the typical meme font onto an image. Text is in the top left corner."""
    draw.text((x - offset, y - offset), text, (0, 0, 0), font = font)
    draw.text((x + offset, y - offset), text, (0, 0, 0), font = font)
    draw.text((x + offset, y + offset), text, (0, 0, 0), font = font)
    draw.text((x - offset, y + offset), text, (0, 0, 0), font = font)
    draw.text((x, y), text, (255, 255, 255), font = font)

def create_meme(text, img, font, pos = "top", spongebob = False):
    """
    Main function of this module.
    Checks whether the text needs multiple lines to fit onto the image
    and splits it accordingly.
    This happens in a way that prevents words from being cut.
    It then uses the above helper function to print the text centered onto the image.
    
    text -- String; the text to be written onto the image.
    pos  -- String; position of the text, either "top" or "bottom" (default is "top").
    img  -- an image; opened via Image.open(URL)
    font -- the font to be used (default is a typical meme font)
    """
    
    fontsize = int(img.height * 0.15)
    offset = int(fontsize * 0.05)
    font_adjusted_size = ImageFont.truetype(font, fontsize)
    draw = ImageDraw.Draw(img)
    
    # If spongebob mode has been turned on, randomly capitalize letters in the text
    if spongebob:
        new = []
        for char in text:
            r = random.randint(0, 1)
            if r: new.append(char.upper())
            else: new.append(char.lower())
        text = ''.join(new)
    else:
        text = text.upper()
    
    # Get the size of the text and use it to determine the number of lines needed
    w, h = draw.textsize(text, font_adjusted_size)
    line_count = 1
    if w > img.width:
        line_count = int(round((w / img.width) + 1))

    print("Number of lines: {}".format(line_count))

    lines = []
    if line_count > 1:

        last_cut = 0
        is_last = False
        for i in range(0, line_count):
            if last_cut == 0:
                cut = round((len(text) / line_count) * i)
            else:
                cut = last_cut

            if i < line_count - 1:
                next_cut = round((len(text) / line_count) * (i + 1))
            else:
                next_cut = len(text)
                is_last = True

            print("cut: {} -> {}".format(cut, next_cut))

            # Make sure we don't cut words in half
            if next_cut == len(text) or text[next_cut] == " ":
                print("Splitting possible!")
            else:
                print("Splitting impossible ...")
                while text[next_cut] != " ":
                    next_cut += 1
                print("new cut: {}".format(next_cut))

            line = text[cut : next_cut].strip()

            # Is line still fitting?
            w, h = draw.textsize(line, font_adjusted_size)
            if not is_last and w > img.width:
                print("overshot")
                next_cut -= 1
                while text[next_cut] != " ":
                    next_cut -= 1
                print("new cut: {}".format(next_cut))

            last_cut = next_cut
            lines.append(text[cut : next_cut].strip())

    else:
        lines.append(text)

    print(lines)

    last_y = -h
    if pos == "bottom":
        last_y = img.height - h * (line_count + 1) - 10

    for i in range(0, line_count):
        w, h = draw.textsize(lines[i], font_adjusted_size)
        x = img.width/2 - w/2
        y = last_y + h
        draw_text(lines[i], draw, font_adjusted_size, x, y, offset)
        last_y = y