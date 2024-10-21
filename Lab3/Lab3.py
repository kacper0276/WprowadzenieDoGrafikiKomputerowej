from PIL import Image
import numpy as np
from PIL.Image import Image as img

# Zad 1

def rysuj_ramki_szare(w, h, grub):
    t = (h, w)
    tab = np.ones(t, np.uint8) * 255

    ile_ramek = min(w, h) // (2 * grub)
    szarosc_krok = 255 // (ile_ramek + 1)

    for i in range(ile_ramek):
        color = i * szarosc_krok
        tab[i * grub:h - i * grub, i * grub:w - i * grub] = color

    return Image.fromarray(tab)

def rysuj_pasy_pionowe_szare(w, h, grub):
    t = (h, w)
    tab = np.ones(t, np.uint8) * 255

    ile = int(w / grub)
    szarosc_krok = 255 // (ile + 1)

    for i in range(ile):
        color = i * szarosc_krok
        tab[:, i * grub:(i + 1) * grub] = color

    return Image.fromarray(tab)


ramka = rysuj_ramki_szare(300, 200, 5)
# ramka.save('ramki_szare.png')
# ramka.show()

pasy = rysuj_pasy_pionowe_szare(300, 200, 5)
# pasy.save('pasy_pionowe_szare.png')
# pasy.show()

# Zad 2

def negatyw(obraz: img):
    imgType = obraz.mode

    if imgType == '1':
        tab = np.asarray(obraz, np.bool_)
    else:
        tab = np.asarray(obraz, np.uint8)

    tab_neg = tab.copy()

    w, h = obraz.size
    if imgType == '1' or imgType == 'L' or imgType == 'RGB':
        for i in range(h):
            for j in range(w):
                if imgType == 'RGB':
                    pixel = tab_neg[i, j]

                    pixel[0] = 255 - pixel[0]

                    pixel[1] = 255 - pixel[1]

                    pixel[2] = 255 - pixel[2]

                    tab_neg[i, j] = pixel
                elif imgType == '1':
                    tab_neg[i, j] = not tab_neg[i, j]
                else:
                    tab_neg[i, j] = 255 - tab_neg[i, j]

    return Image.fromarray(tab_neg)



def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)


def rysuj_po_skosie_szare(h,w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


gwizadka = Image.open('gwiazdka.bmp')
negatyw_gwiazdka = negatyw(gwizadka)

# gwizadka.show()
# negatyw_gwiazdka.show()
# negatyw_gwiazdka.save('negatyw_gwiazdka.png')

ramki_kolorowe = rysuj_ramki_kolorowe(200, [20, 120,220], 6, 6, -6)
# ramki_kolorowe.show()
# ramki_kolorowe.save('ramki_kolorowe.png')
negatyw_ramki_kolorowe = negatyw(ramki_kolorowe)
# negatyw_ramki_kolorowe.show()
# negatyw_ramki_kolorowe.save('negatyw_ramki_kolorowe.png')

po_skosie = rysuj_po_skosie_szare(100, 300, 6, 6)
# po_skosie.show()
# po_skosie.save('po_skosie.png')
po_skosie_negatyw = negatyw(po_skosie)
# po_skosie_negatyw.show()
# po_skosie_negatyw.save('negatyw_po_skosie.png')

# Zad 3

def koloruj_w_paski(obraz: img, grub, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    w, h = obraz.size

    tab = np.ones((h, w, 3), dtype=np.uint8) * 255

    r, g, b = kolor

    for y in range(h):
        if y % grub == 0:
            r = max(0, min(255, r + zmiana_koloru_r))
            g = max(0, min(255, g + zmiana_koloru_g))
            b = max(0, min(255, b + zmiana_koloru_b))

        for x in range(w):
            if obraz.getpixel((x, y)) == 0:
                tab[y, x] = [r, g, b]

    nowy_obraz = Image.fromarray(tab)
    return nowy_obraz


obraz = Image.open('../Lab1/inicjaly.bmp')
# print(obraz.mode)
koloruj = koloruj_w_paski(obraz, 5, [20, 120,220], 6, 6, -6)

# koloruj.save('zad_3.png')
# koloruj.save('zad_3.jpg')

# koloruj.show()

# Zadanie 4
ex4 = Image.new("RGB", (100, 100))

pixel_data = np.array(ex4)

# pixel_data[0,0] = 328
# pixel_data[0,0] = -28

def uint8_wrap(value):
    if value < 0:
        return value + 256
    return value % 256

print(uint8_wrap(-24))

print(uint8_wrap(328))
