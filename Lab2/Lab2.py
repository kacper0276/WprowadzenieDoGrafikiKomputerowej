from PIL import Image
import numpy as np

# Zadanie 2

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
def rysuj_wlasne(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * 255

    for y in range(0, h, grub):
        for x in range(0, w, grub):
            if (x // grub + y // grub) % 2 == 0:
                tab[y:y + grub, x:x + grub] = 0

    return Image.fromarray(tab)

obrazek = Image.open('inicjaly.bmp')
# zmiana = rysuj_ramke_w_obrazie(obrazek, 1)
# zmiana.show()

# pionowe_pasy = rysuj_pasy_pionowe(100, 50, 50)
# pionowe_pasy.show()

# ramka = rysuj_ramki(100, 50, 2)
# ramka.show()

# szachownica = rysuj_wlasne(50, 50, 1)
# szachownica.show()

# Zadanie 3

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_bazowa = np.asarray(obraz_bazowy).astype(np.uint8)
    tab_wstawiana = np.asarray(obraz_wstawiany).astype(np.uint8)

    h_bazowa, w_bazowa = tab_bazowa.shape
    h_wstawiana, w_wstawiana = tab_wstawiana.shape

    n_k = min(h_bazowa, n + h_wstawiana)
    m_k = min(w_bazowa, m + w_wstawiana)
    n_p = max(0, n)
    m_p = max(0, m)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowa[i][j] = tab_wstawiana[i - n][j - m]

    # Konwersja z powrotem do obrazu
    tab_bazowa = tab_bazowa * 255
    nowy_obraz = Image.fromarray(tab_bazowa)

    return nowy_obraz

wstawiany = Image.open('../Lab1/inicjaly.bmp')
bazowy = Image.new('L', (300, 200), 0)

nowy_obraz = wstaw_obraz_w_obraz(bazowy, wstawiany, 100, 50)

nowy_obraz.show()