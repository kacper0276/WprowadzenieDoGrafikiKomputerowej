from random import randint

from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad1
zad1 = Image.open('plikidokolokwium/obrazki/bek4.png')
s = stat.Stat(zad1)

print("stddev ", s.stddev)

zad11 = Image.open('plikidokolokwium/obrazki/bek2.png')
s11 = stat.Stat(zad11)
print("median ", s11.median)

zad12 = Image.open('plikidokolokwium/obrazki/bek3.png')
s22 = stat.Stat(zad12)
print("mean ", s22.mean)

# Zad 2
def rysuj_ramke_kolor(w, h, grub, r, g, b):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = 255, 0, 0
    tab[grub:h-grub, grub:w-grub] = r, g, b
    return tab

# Image.fromarray(rysuj_ramke_kolor(120, 60, 10, 100, 200, 30)).show()

# Zad 3
tablica = np.loadtxt('plikidokolokwium/tablice/tab2.txt', dtype=np.bool_)
# a = Image.fromarray(tablica)
# a.show()

batman_image = Image.open('plikidokolokwium/obrazki/batman2.png')
batman_pixels = np.array(batman_image)

wys, szer = tablica.shape

x_offset = batman_image.width - szer
y_offset = 0

for i in range(wys):
    for j in range(szer):
        if tablica[i, j] == 1:
            batman_pixels[y_offset + i, x_offset + j] = [0, 0, 0]
        else:
            batman_pixels[y_offset + i, x_offset + j] = [255, 0, 0]

batman_image = Image.fromarray(batman_pixels)

batman_image.save('batman_with_tab_image.png')

# batman_image.show()

# image_from_tab = Image.fromarray(np.uint8(t1 * 255))
#
# for i in range(wys):
#     for j in range(szer):
#         if image_from_tab[j, i] == 255:  # Biały
#             image_from_tab[j, i] = (0, 0, 0)  # Zamień na czarny
#         elif image_from_tab[j, i] == 0:  # Czarny
#             image_from_tab[j, i] = (255, 0, 0)

# Zad 4
def ocena_identycznosci(obraz1, obraz2):

    if obraz1.size != obraz2.size:
        return f"Obrazy mają różne rozmiary: {obraz1.size} vs {obraz2.size}"

    roznica = ImageChops.difference(obraz1, obraz2)
    roznica_array = np.array(roznica)

    suma_roznic = np.sum(roznica_array)

    maks_roznica = np.max(roznica_array)

    liczba_roznic = np.count_nonzero(roznica_array)

    if suma_roznic == 0:
        return "Obrazy są identyczne"
    else:
        return {
            "Suma różnic": suma_roznic,
            "Maksymalna różnica": maks_roznica,
            "Liczba różniących się pikseli": liczba_roznic
        }

zad41 = Image.open('plikidokolokwium/mono/mono3.png')
zad42 = Image.open('plikidokolokwium/mono/mono11.bmp')

# print(ocena_identycznosci(zad41, zad42))

# Zad 5
def check_channel_permutation(image1, image2):
    r1, g1, b1 = image1.split()

    if Image.merge('RGB', (r1, g1, b1)) == image2:
        return "No channel change."
    elif Image.merge('RGB', (r1, b1, g1)) == image2:
        return "Channels swapped: G and B."
    elif Image.merge('RGB', (g1, r1, b1)) == image2:
        return "Channels swapped: R and G."
    elif Image.merge('RGB', (g1, b1, r1)) == image2:
        return "Channels swapped: R and B."
    elif Image.merge('RGB', (b1, r1, g1)) == image2:
        return "Channels swapped: R and B, G and R."
    elif Image.merge('RGB', (b1, g1, r1)) == image2:
        return "Channels swapped: R and B, G and B."
    else:
        return "No matching channel permutation found."

def check_negative(image1, image2):
    inverted_image1 = ImageChops.invert(image1)
    return inverted_image1 == image2

def is_negative(original, mix):
    return np.all(mix == 255 - original)

obraz = Image.open('plikidokolokwium/obrazki/batman3.png')
mix = Image.open('plikidokolokwium/mix/mix23.png')

# Zad 6
def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    # plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    # plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


im61 = Image.open('plikidokolokwium/obrazki/bek1.png')
im62 = Image.open('plikidokolokwium/obrazki/bek2.png')
im63 = Image.open('plikidokolokwium/obrazki/bek3.png')

# rysuj_histogram_RGB(im61)
# rysuj_histogram_RGB(im62)
# rysuj_histogram_RGB(im63)

# Zad 7

def szary(w, h, a, b):
    tab = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i**2 + b * j**2) % 256
    return tab

bek1 = Image.open("plikidokolokwium/obrazki/bek1.png")
w, h = bek1.size

szary_obraz = szary(w, h, 3, -1)
szary_pil = Image.fromarray(szary_obraz)
szary_pil.show()

bek1_array = np.array(bek1)
r, g, b = bek1.split()
g = szary_pil
# bek1_array[:, :, 1] = szary_obraz
wynikowy_obraz = Image.merge('RGB', (r, g, b))
mix = Image.fromarray(bek1_array)
# mix.save("mix.png")
# mix.show()

# Zad 8

im81 = Image.open('plikidokolokwium/obrazki/im1.bmp')
print(im81.mode)
im81Arr = np.array(im81)

print(im81Arr[50][100])
print('ASDASDAAAAA',im81.getpixel((100, 50)))

im82 = Image.open('plikidokolokwium/obrazki/im4.bmp')
print(im82.mode)
im82Arr = np.asarray(im82)
print('ADADASDA',im82.size)
print(im82Arr.shape)

print("rozmiar", im81.size)

print(im82.getpixel((50, 100)))

# Zad 9
def odczytaj_kod(obraz, zakodowany):
    t_obraz = np.asarray(obraz)
    t_zakodowany = np.asarray(zakodowany)
    h, w, d = t_obraz.shape

    im_kod = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            for k in range(d):
                if t_zakodowany[i, j, k] > t_obraz[i, j, k]:
                    im_kod[i, j] = 1
                    break

    return im_kod

obraz = Image.open("plikidokolokwium/obrazki/batman2.png")
zakodowany_obraz = Image.open("plikidokolokwium/obrazki/zakodowany2_2.png")

im_kod = odczytaj_kod(obraz, zakodowany_obraz)
Image.fromarray(im_kod * 255).save('im_kod.png')

czarne_piksele = np.sum(im_kod == 0)
print(czarne_piksele)

def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod).astype(np.uint8)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] == 0:
                k = randint(0,2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)

im = ukryj_kod(obraz, im_kod)
im.show()