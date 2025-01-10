from PIL import Image
import numpy as np
from PIL import ImageOps, ImageChops
import matplotlib.pyplot as plt
from PIL import ImageStat as stat

# Zad 1
obraz1 = Image.open("messi.jpg")
obraz2 = Image.open("olsztyn.jpg").resize(obraz1.size)

alpha = 2 / (2 + 3)
mix = Image.blend(obraz1, obraz2, alpha=alpha)

mix.show()

# Zad 2

left, top, right, bottom = 100, 100, 300, 300
fragment = obraz1.crop((left, top, right, bottom))

obraz2.paste(fragment, (50, 50))
obraz2.show()