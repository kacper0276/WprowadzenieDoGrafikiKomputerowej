from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('baby_yoda.jpg')

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)

    max_vals = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            max_vals[0] = max(max_vals[0], pixel[0])
            max_vals[1] = max(max_vals[1], pixel[1])
            max_vals[2] = max(max_vals[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (max_vals[0], max_vals[1], max_vals[2])

    return obraz1

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)

    min_vals = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            min_vals[0] = min(min_vals[0], pixel[0])
            min_vals[1] = min(min_vals[1], pixel[1])
            min_vals[2] = min(min_vals[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (min_vals[0], min_vals[1], min_vals[2])

    return obraz1

miejsca = [(100, 150), (250, 300), (50, 100)]
dlugosci = [15, 25, 35]

obraz1 = obraz.copy()
for m, n in miejsca:
    for k in dlugosci:
        obraz1 = rysuj_kwadrat_max(obraz1, m, n, k)

obraz1.save('obraz1.png')

obraz2 = obraz.copy()
for m, n in miejsca:
    for k in dlugosci:
        obraz2 = rysuj_kwadrat_min(obraz2, m, n, k)

obraz2.save('obraz2.png')

plt.figure(figsize=(10, 5))

obraz1 = Image.open('obraz1.png')
obraz2 = Image.open('obraz2.png')

plt.subplot(1, 2, 1)
plt.imshow(obraz1)
plt.title('Obraz z kwadratami (max)')

plt.subplot(1, 2, 2)
plt.imshow(obraz2)
plt.title('Obraz z kwadratami (min)')

plt.show()

# Zadanie 2
def rysuj_kolo_z_pikseli(obraz, m_s, n_s, r, x, y, szerokosc, wysokosc):
    obraz1 = obraz.copy()
    w, h = obraz.size

    fragment = obraz.crop((x, y, x + szerokosc, y + wysokosc))

    for i in range(w):
        for j in range(h):
            if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:
                fi = (i - m_s) % szerokosc
                fj = (j - n_s) % wysokosc
                kolor_fragmentu = fragment.getpixel((fi, fj))
                obraz1.putpixel((i, j), kolor_fragmentu)

    return obraz1

# Zadanie 3
def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = im.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img