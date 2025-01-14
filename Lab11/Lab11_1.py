from PIL import Image, ImageDraw, ImageFont, ImageColor
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
import math

# Zad 1
obraz1 = Image.open("messi.jpg")
obraz2 = Image.open("olsztyn.jpg").resize(obraz1.size)

alpha = 2 / (2 + 3)
mix = Image.blend(obraz1, obraz2, alpha=alpha)

# mix.show()

# Zad 2
left, top, right, bottom = 100, 100, 300, 300
fragment = obraz1.crop((left, top, right, bottom))

obraz2.paste(fragment, (50, 50))
# obraz2.show()

# Zad 3
obrazEx3 = Image.open('Shrek_Fiona.png')
text = "Jedi używa Mocy do zdobywania wiedzy i obrony, nigdy do ataku"
# fnt = ImageFont.truetype("ttf/DejaVuSansDisplay.ttf", 30)
# d = ImageDraw.Draw(obrazEx3)
# color = ImageColor.getrgb("#7fff00")
# d.text((40,40), text, font=fnt, fill=color, align ="left")

# obrazEx3.show()

# Zad 4
image = Image.new("RGB", (200, 100), "blue")
draw = ImageDraw.Draw(image)

draw.ellipse((10, 10, 90, 90), outline="#ff69b4", width=5)

draw.ellipse((110, 10, 190, 90), outline="#0096eb", width=5)

# image.save("obraz_okregi.png")

image2 = Image.new("RGB", (200, 100), "white")
draw2 = ImageDraw.Draw(image2)

draw2.rectangle((0, 0, 199, 99), outline="black", width=1)

left_diamond = [(50, 0), (0, 50), (50, 100), (100, 50)]
draw2.polygon(left_diamond, outline="black", fill=None)

right_diamond = [(150, 0), (100, 50), (150, 100), (200, 50)]
draw2.polygon(right_diamond, outline="black", fill=None)

image2.show()

# image2.save("obraz_diamenty_ramka.png")