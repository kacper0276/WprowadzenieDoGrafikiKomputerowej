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

# wynikowy_obraz.save('obraz_inicjaly.png')

# Zadanie 2

obrazek_zad2 = Image.open('obraz.png')
obrazek_zad2.save("zad2/obraz1.jpg")

for i in range(1, 5):
    obraz = Image.open(f"zad2/obraz{i}.jpg")
    obraz.save(f"zad2/obraz{i+1}.jpg")

obraz = Image.open("obraz.png")
obraz5 = Image.open("zad2/obraz5.jpg")

histogram_oryginal = obraz.histogram()
histogram_obraz5 = obraz5.histogram()
roznica_obraz = ImageChops.difference(obraz, obraz5)

histogram_roznica = roznica_obraz.histogram()

plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Oryginalny obraz")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(obraz5)
plt.title("Obraz5")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(roznica_obraz)
plt.title("Obraz różnicy")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(histogram_oryginal, label="Oryginalny obraz", color='blue', alpha=0.7)
plt.plot(histogram_obraz5, label="Obraz5", color='green', alpha=0.7)
plt.title("Histogramy")
plt.legend()

# plt.savefig('zad2/porownanie_org_obr5')

obraz4 = Image.open("zad2/obraz4.jpg")
obraz4_histogram = obraz4.histogram()
roznica_obraz4_obraz5 = ImageChops.difference(obraz4, obraz5)

plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.imshow(obraz4)
plt.title("Obraz 4")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(obraz5)
plt.title("Obraz 5")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(roznica_obraz4_obraz5)
plt.title("Różnica obrazów 4 i 5")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(obraz4_histogram, bins=256, color='blue', alpha=0.7, label="Obraz 4")
plt.hist(histogram_obraz5, bins=256, color='green', alpha=0.7, label="Obraz 5")
plt.title("Histogramy obrazów")
plt.legend()

# plt.savefig('zad2/porownanie_obr4_obr5_hist')

# Zadanie 3

def odkoduj(obraz1, obraz2):
    szerokosc, wysokosc = obraz1.size

    tablica1 = np.array(obraz1)
    tablica2 = np.array(obraz2)

    roznice = np.zeros((wysokosc, szerokosc), dtype=np.uint8)

    for y in range(wysokosc):
        for x in range(szerokosc):
            if (tablica1[y, x, 0] != tablica2[y, x, 0] or
                    tablica1[y, x, 1] != tablica2[y, x, 1] or
                    tablica1[y, x, 2] != tablica2[y, x, 2]):
                roznice[y, x] = 255

    wynikowy_obraz = Image.fromarray(roznice)

    return wynikowy_obraz


test = Image.open('pliki/jesien.jpg')
test_zakodowany = Image.open('pliki/zakodowany1.bmp')

testowy = odkoduj(test, test_zakodowany)

# testowy.show()

obraz_jesien = Image.open('pliki/jesien.jpg')
obraz_zakodowany2 = Image.open('pliki/zakodowany2.bmp')

odkodowany = odkoduj(obraz_jesien, obraz_zakodowany2)

# odkodowany.show()
odkodowany.save('pliki/kod2.bmp')