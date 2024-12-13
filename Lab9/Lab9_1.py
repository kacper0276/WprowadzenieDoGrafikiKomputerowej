from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad 1
obraz = Image.open("zeby.png").convert("L")

# Zad 2
def histogram_norm(obrazi):
    hist = np.zeros(256, dtype=np.float32)
    for value in obrazi.flat:
        hist[value] += 1
    norm_hist = hist / hist.sum()
    return norm_hist

def histogram_cumul(obraz):
    norm_hist = histogram_norm(obraz)
    cumul_hist = np.zeros_like(norm_hist)
    cumul_value = 0
    for i in range(len(norm_hist)):
        cumul_value += norm_hist[i]
        cumul_hist[i] = cumul_value
    return cumul_hist

def histogram_equalization(obraz):
    cumul_hist = histogram_cumul(obraz)
    lut = (cumul_hist * 255).astype(np.uint8)
    equalized_image = lut[obraz]
    return equalized_image


# Zad 3
imEx3 = ImageOps.equalize(obraz)

imEx3.save("equalized1.png")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(obraz)
plt.title('')

plt.subplot(1, 2, 2)
plt.imshow(imEx3)
plt.title('Obraz z kwadratami (min)')