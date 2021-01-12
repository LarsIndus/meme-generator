# Simple meme generator
# Source: https://blog.lipsumarium.com/caption-memes-in-python/

from PIL import ImageFont, ImageDraw
from PIL.Image import Image
from typing import Optional
import random

class Meme:
    def __init__(self, img: Optional[Image] = None,
                 txt_top: str = "", txt_bottom: str = "",
                 spongebob: bool = False, font: str = "impact.ttf") -> None:
        self.img = img
        self.txt_top = txt_top
        self.txt_bottom = txt_bottom
        self.spongebob = spongebob
        self.font = font

        if self.img is not None:
            self.create_meme()

    def create_meme(self) -> None:
        self.print_top_bottom(self.txt_top, "top")
        self.print_top_bottom(self.txt_bottom, "bottom")

    def print_top_bottom(self, text: str, pos: str = "top") -> None:
        """
        Main method of this class.
        Checks whether the text needs multiple lines to fit onto the image
        and splits it accordingly.
        This happens in a way that prevents words from being cut.
        It then uses the helper method '_draw_text' to print the text
        centered onto the image.
        
        text -- String; the text to be written onto the image.
        pos  -- String; position of the text, either "top" or "bottom"
                (default is "top").
        """
        
        if self.img is None:
            print("No image supplied!")
            return

        fontsize = int(self.img.height * 0.15)
        offset = int(fontsize * 0.05)
        font_adjusted_size = ImageFont.truetype(self.font, fontsize)
        draw = ImageDraw.Draw(self.img)
        
        # If spongebob mode has been turned on,
        # randomly capitalize letters in the text
        if self.spongebob:
            new = []
            for char in text:
                r = random.randint(0, 1)
                if r: new.append(char.upper())
                else: new.append(char.lower())
            text = ''.join(new)
        else:
            text = text.upper()
        
        # Get the size of the text and use it to determine the number of lines
        w, h = draw.textsize(text, font_adjusted_size)
        line_count = 1
        if w > self.img.width:
            line_count = int(round((w / self.img.width) + 1))

        print("Number of lines: {}".format(line_count))

        lines = []
        if line_count > 1:

            last_cut = 0
            is_last = False
            for i in range(line_count):
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
                if not is_last and w > self.img.width:
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
            last_y = self.img.height - h * (line_count + 1) - 10

        for i in range(line_count):
            w, h = draw.textsize(lines[i], font_adjusted_size)
            x = (self.img.width / 2) - (w / 2)
            y = last_y + h
            self._draw_text(lines[i], x, y, offset, font_adjusted_size)
            last_y = y

    # internal use only
    def _draw_text(self, text: str, x: float, y: float,
                   offset: float, font: str) -> None:
        """
        Prints font onto an image. Text is in the top left corner.
        Default font is a typical meme font.
        """
        draw = ImageDraw.Draw(self.img)

        draw.text((x - offset, y - offset), text, (0, 0, 0), font)
        draw.text((x + offset, y - offset), text, (0, 0, 0), font)
        draw.text((x + offset, y + offset), text, (0, 0, 0), font)
        draw.text((x - offset, y + offset), text, (0, 0, 0), font)
        draw.text((x, y), text, (255, 255, 255), font)

    def show_image(self):
        self.img.show()

