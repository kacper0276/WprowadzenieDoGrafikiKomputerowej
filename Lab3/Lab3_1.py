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
# ramka.show()

pasy = rysuj_pasy_pionowe_szare(300, 200, 5)
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

ramki_kolorowe = rysuj_ramki_kolorowe(200, [20, 120,220], 6, 6, -6)
# ramki_kolorowe.show()
negatyw_ramki_kolorowe = negatyw(ramki_kolorowe)
# negatyw_ramki_kolorowe.show()

po_skosie = rysuj_po_skosie_szare(100, 300, 6, 6)
# po_skosie.show()
po_skosie_negatyw = negatyw(po_skosie)
# po_skosie_negatyw.show()

# Zad 3

def koloruj_w_paski(obraz, grub):
    print(obraz.size)