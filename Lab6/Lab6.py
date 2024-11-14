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

ma = obraz.width - inicjaly.width
na = obraz.height - inicjaly.height
obraz1 = wstaw_inicjaly(obraz, inicjaly, ma, na, (255, 0, 0))
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

mb = (obraz.width - inicjaly.width) // 2
nb = (obraz.height - inicjaly.height) // 2
obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, mb, nb)
# obraz2.show()

# Zad 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz_copy = obraz.copy()
    obraz_pixels = obraz_copy.load()
    initials_pixels = inicjaly.load()
    width, height = inicjaly.size
    for x in range(width):
        for y in range(height):
            if initials_pixels[x, y] == 0:
                obraz_pixels[m + x, n + y] = kolor
    return obraz_copy

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):
    obraz_copy = obraz.copy()
    obraz_pixels = obraz_copy.load()
    initials_pixels = inicjaly.load()
    width, height = inicjaly.size
    for x in range(width):
        for y in range(height):
            if initials_pixels[x, y] == 0:
                r, g, b = obraz_pixels[m + x, n + y]
                obraz_pixels[m + x, n + y] = (255 - r, 255 - g, 255 - b)
    return obraz_copy

obraz3 = wstaw_inicjaly_load(obraz, inicjaly, ma, na, (255, 0, 0))
obraz4 = wstaw_inicjaly_maska_load(obraz, inicjaly, mb, nb)

plt.figure(figsize=(16, 16))
plt.subplot(1, 2, 1)
plt.imshow(obraz3)
plt.title("Obraz 3")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(obraz4)
plt.title("Obraz 4")
plt.axis('off')

plt.title('Zadanie 3')
# plt.show()
# plt.savefig('fig1.png')

