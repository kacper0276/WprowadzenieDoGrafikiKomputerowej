from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad 1
obraz = Image.open("zeby.png").convert("L")

# Zad 2
def histogram_norm(obraz):
    obraz_array = np.asarray(obraz)
    histogram = np.histogram(obraz_array, bins=256, range=(0, 256))[0]
    histogram_normalized = histogram / np.sum(histogram)
    return histogram_normalized

def histogram_cumul(obraz):
    norm_hist = histogram_norm(obraz)
    cumul_hist = np.zeros_like(norm_hist)
    cumul_value = 0
    for i in range(len(norm_hist)):
        cumul_value += norm_hist[i]
        cumul_hist[i] = cumul_value
    return cumul_hist

def histogram_equalization(obraz):
    obraz_array = np.asarray(obraz)
    cumul_hist = histogram_cumul(obraz)
    lut = (cumul_hist * 255).astype(np.uint8)
    equalized_image = Image.fromarray(lut[obraz_array])
    return equalized_image

im21 = histogram_norm(obraz)
im22 = histogram_cumul(obraz)
im23 = histogram_equalization(obraz)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(np.asarray(obraz).ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
plt.title("Histogram Oryginalny")

plt.subplot(2, 2, 2)
plt.plot(im21, color='green')
plt.title("Histogram Znormalizowany")

plt.subplot(2, 2, 3)
plt.plot(im22, color='orange')
plt.title("Histogram Skumulowany")

plt.subplot(2, 2, 4)
plt.hist(np.asarray(im23).ravel(), bins=256, range=(0, 256), color='red', alpha=0.7)
plt.title("Histogram Wyrównany")

plt.tight_layout()
plt.savefig("fig1.png")
# plt.show()

obraz = Image.open("zeby.png").convert("L")

obraz_equalized = ImageOps.equalize(obraz)
obraz_equalized.save('equalized.png')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(obraz, cmap='gray')
plt.title("Oryginalny Obraz")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(obraz_equalized, cmap='gray')
plt.title("Obraz po wyrównaniu histogramu")
plt.axis("off")

plt.tight_layout()
plt.show()

# Zad 3
imEx3 = ImageOps.equalize(obraz)

imEx3.save("equalized1.png")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(obraz_equalized)
plt.title('')

plt.subplot(1, 2, 2)
plt.imshow(imEx3)
plt.title('Obraz z kwadratami (min)')

plt.savefig("fig2.png")

# Zad 4
def konwertuj1(obraz, w_r, w_g, w_b):
    piksele = obraz.load()
    szerokosc, wysokosc = obraz.size

    nowy_obraz = Image.new("L", (szerokosc, wysokosc))
    piksele_nowy = nowy_obraz.load()

    for x in range(szerokosc):
        for y in range(wysokosc):
            r, g, b = piksele[x, y]
            l = round(r * w_r + g * w_g + b * w_b)
            piksele_nowy[x, y] = l

    return nowy_obraz

def konwertuj2(obraz, w_r, w_g, w_b):
    piksele = obraz.load()
    szerokosc, wysokosc = obraz.size

    nowy_obraz = Image.new("L", (szerokosc, wysokosc))
    piksele_nowy = nowy_obraz.load()

    for x in range(szerokosc):
        for y in range(wysokosc):
            r, g, b = piksele[x, y]
            l = int(r * w_r + g * w_g + b * w_b)
            piksele_nowy[x, y] = l

    return nowy_obraz

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

w_r = 299 / 1000
w_g = 587 / 1000
w_b = 114 / 1000

sciezka_wejsciowa = "mgla.jpg"
obraz = Image.open(sciezka_wejsciowa).convert("RGB")

obraz_L1 = konwertuj1(obraz, w_r, w_g, w_b)
obraz_L1.save("mgla_L1.png")

obraz_L = obraz.convert("L")
obraz_L.save("mgla_L.png")

obraz_L2 = konwertuj2(obraz, w_r, w_g, w_b)
obraz_L2.save("mgla_L2.png")

print('OBRAZ')
statystyki(obraz)
print('obraz_L')
statystyki(obraz_L)
print('obraz_L1')
statystyki(obraz_L1)
print('obraz_L2')
statystyki(obraz_L2)