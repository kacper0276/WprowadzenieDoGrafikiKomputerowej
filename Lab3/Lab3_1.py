from PIL import Image
import numpy as np

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
ramka.show()

pasy = rysuj_pasy_pionowe_szare(300, 200, 5)
pasy.show()
