from PIL import Image
import numpy as np

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape

    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0

    for i in range(grub):
        for j in range(w):
            tab_obraz[i][j] = 0

    for i in range(h - grub, h):
        for j in range(w):
            tab_obraz[i][j] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)


def rysuj_ramki(w,h,grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)


def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, np.uint8) * 255

    ile = int(w / grub)

    for i in range(ile):
        if i % 2 == 0:
            tab[:, i * grub:(i + 1) * grub] = 0

    return Image.fromarray(tab)


def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, np.uint8) * 255

    ile_ramek = min(w, h) // (2 * grub)

    for i in range(ile_ramek):
        color = 0 if i % 2 == 0 else 255
        tab[i * grub:h - i * grub, i * grub:w - i * grub] = color

    return Image.fromarray(tab)

# Rysuje szachownicę gdzie kwadraty mają grubość podaną w argumencie grub
import numpy as np
from PIL import Image


def rysuj_wlasne(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * 255

    for y in range(0, h, grub):
        for x in range(0, w, grub):
            if (x // grub + y // grub) % 2 == 0:
                tab[y:y + grub, x:x + grub] = 0

    return Image.fromarray(tab)

# obrazek = Image.open('bs.bmp')
# zmiana = rysuj_ramke_w_obrazie(obrazek, 1)
# zmiana.show()

# pionowe_pasy = rysuj_pasy_pionowe(100, 50, 50)
# pionowe_pasy.show()

# ramka = rysuj_ramki(100, 50, 2)
# ramka.show()

szachownica = rysuj_wlasne(50, 50, 1)
szachownica.show()