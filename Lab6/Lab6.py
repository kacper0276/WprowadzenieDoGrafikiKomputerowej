from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Zad 1
obraz = Image.open('obraz.png')
inicjaly = Image.open('inicjaly.bmp')

# Zad 2
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obraz_copy = obraz.copy()
    width, height = inicjaly.size
    for x in range(width):
        for y in range(height):
            if inicjaly.getpixel((x, y)) == 0:
                obraz_copy.putpixel((m + x, n + y), kolor)
    return obraz_copy

m = obraz.width - inicjaly.width
n = obraz.height - inicjaly.height
obraz1 = wstaw_inicjaly(obraz, inicjaly, m, n, (255, 0, 0))
# obraz1.show()

def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    obraz_copy = obraz.copy()
    width, height = inicjaly.size
    for x in range(width):
        for y in range(height):
            if inicjaly.getpixel((x, y)) == 0:
                r, g, b = obraz_copy.getpixel((m + x, n + y))
                obraz_copy.putpixel((m + x, n + y), (255 - r, 255 - g, 255 - b))
    return obraz_copy

m = (obraz.width - inicjaly.width) // 2
n = (obraz.height - inicjaly.height) // 2
obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, m, n)
# obraz2.show()

# Zad 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    return None

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    return None

