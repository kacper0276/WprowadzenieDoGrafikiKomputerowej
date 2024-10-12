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

# Rysuje szachownicę gdzie kwadraty mają wymiar podany w argumencie grub
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

# wstawiany = Image.open('../Lab1/inicjaly.bmp')
# bazowy = Image.new('L', (300, 200), 0)
#
# nowy_obraz = wstaw_obraz_w_obraz(bazowy, wstawiany, 100, 50)
#
# nowy_obraz.show()

# bazowy = rysuj_pasy_pionowe(300, 200, 15)
# wstawiony = Image.open('inicjaly.bmp')
#
# nowy_obraz_1 = wstaw_obraz_w_obraz(bazowy, wstawiony, 250, 100)
#
# nowy_obraz_1.show()
#
# nowy_obraz_2 = wstaw_obraz_w_obraz(bazowy, wstawiony, 0, 50)
# nowy_obraz_2.show()

#
# ex2 = rysuj_pasy_pionowe(200, 100, 10)
#
# image_path = 'stripes.bmp'
# ex2.save(image_path)
#
# edited_image = Image.open('stripes_256.bmp')
#
# # Step 3: Get image mode and specific pixel values
# tryb_obrazu = edited_image.mode
# pixel_66_13 = edited_image.getpixel((12, 65))
# pixel_97_20 = edited_image.getpixel((97, 20))
#
# print(tryb_obrazu)
#
# # Step 4: Print the required values
# print(f'{tryb_obrazu}; {pixel_66_13}; {pixel_97_20}')

# Ex3 = rysuj_wlasne(100, 100, 5)
#
# Ex3.show()

# Ex4 = np.loadtxt("tablica.txt", dtype=np.bool_)
#
# # Utworzenie obrazu w trybie '1' (obraz binarny)
# obraz = Image.fromarray(Ex4)
#
# obraz_z_ramka = rysuj_ramke_w_obrazie(obraz, 40)
#
# print(obraz.mode)
#
# # Pokaż obraz bez ramki (opcjonalnie)
# obraz_z_ramka.show()

# Ex5 = rysuj_ramki(80, 130, 5)
# name = 'ex5.bmp'
# Ex5.save(name)

# obraz_png = Image.open("ex5.PNG")
#
# tryb_obrazu = obraz_png.mode
# rozmiar_obrazu = obraz_png.size
#
# tablica = np.asarray(obraz_png)
#
# wymiar_tablicy = tablica.shape
# liczba_elementow_tablicy = tablica.size
#
# print(tablica[6][6])
#
# print(f"{tryb_obrazu}; {rozmiar_obrazu}; {wymiar_tablicy}; {liczba_elementow_tablicy}")