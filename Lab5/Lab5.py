from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zadanie 1

def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n,kolor):
    bazowy_w, bazowy_h = obraz_bazowy.size
    wstawiany_w, wstawiany_h = obraz_wstawiany.size

    obraz_bazowy_np = np.array(obraz_bazowy)
    obraz_wstawiany_np = np.array(obraz_wstawiany)

    if m + wstawiany_w > bazowy_w:
        wstawiany_w = bazowy_w - m
    if n + wstawiany_h > bazowy_h:
        wstawiany_h = bazowy_h - n

    for i in range(wstawiany_h):
        for j in range(wstawiany_w):
            if obraz_wstawiany_np[i, j] == 0:
                obraz_bazowy_np[n + i, m + j] = kolor

    obraz_bazowy_wynik = Image.fromarray(obraz_bazowy_np)

    return obraz_bazowy_wynik


obraz_wstawiany = Image.open('inicjaly.bmp') # Obraz w trybie 1
obraz_bazowy = Image.open('obraz.png')

# Prawy górny
wynikowy_obraz = wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, obraz_bazowy.width - obraz_wstawiany.width, 0, [172, 47, 253])

# Lewy dolny
wynikowy_obraz = wstaw_inicjaly(wynikowy_obraz, obraz_wstawiany, 0, obraz_bazowy.height - obraz_wstawiany.height, [255, 255, 255])

# W połowie wysokości tak, żeby było widać tylko pierwszą literę inicjałów
wynikowy_obraz = wstaw_inicjaly(wynikowy_obraz, obraz_wstawiany, obraz_bazowy.width - obraz_wstawiany.width // 2, (obraz_bazowy.height // 2) - (obraz_wstawiany.height // 2), [0, 255, 126])

wynikowy_obraz.save('obraz_inicjaly.png')
