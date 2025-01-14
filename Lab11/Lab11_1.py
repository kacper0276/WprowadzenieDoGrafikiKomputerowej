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
fnt = ImageFont.truetype("ttf/DejaVuSansDisplay.ttf", 30)
d = ImageDraw.Draw(obrazEx3)
color = ImageColor.getrgb("#7fff00")
d.text((40,40), text, font=fnt, fill=color, align ="left")

obrazEx3.show()