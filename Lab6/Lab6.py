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

# Zad 4
def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)

obrazk1 = kontrast(obraz, 15)
obrazk2 = kontrast(obraz, 60)
obrazk3 = kontrast(obraz, 100)

plt.figure(figsize=(16, 16))
plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Obraz")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(obrazk1)
plt.title("Kontrast 1")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(obrazk2)
plt.title("Kontrast 2")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(obrazk3)
plt.title("Kontrast 3")
plt.axis('off')

# plt.show()
# plt.savefig('fig2.png')

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))

logImg = transformacja_logarytmiczna(obraz)

a, b = 2, 100
obraz4a = obraz.copy().point(lambda i: a * i + b)

plt.figure(figsize=(16, 16))
plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Obraz")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(logImg)
plt.title('LogImg')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(obraz4a)
plt.title('Obraz 4AB')
plt.axis('off')

# plt.show()
# plt.savefig('fig3.png')

def transformacja_gamma (obraz, gamma):
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)

obraz4c1 = transformacja_gamma(obraz, .5)
obraz4c2 = transformacja_gamma(obraz, 1)
obraz4c3 = transformacja_gamma(obraz, 5)

plt.figure(figsize=(16, 16))
plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Obraz")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(obraz4c1)
plt.title("Kontrast 1")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(obraz4c2)
plt.title("Kontrast 2")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(obraz4c3)
plt.title("Kontrast 3")
plt.axis('off')

# plt.show()
# plt.savefig('fig4.png')

# Zad 5
def add_constant_to_array(obraz, value):
    array = np.array(obraz, dtype=np.uint8)
    width, height = obraz.size
    for x in range(width):
        for y in range(height):
            array[y, x] = min(array[y, x] + value, 255)
    return Image.fromarray(array)