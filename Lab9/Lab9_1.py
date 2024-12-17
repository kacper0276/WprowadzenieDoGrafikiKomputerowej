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
plt.show()

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

# Zad 4
def konwertuj1(obraz, w_r, w_g, w_b):
    assert 0 <= w_r <= 1 and 0 <= w_g <= 1 and 0 <= w_b <= 1, "Weights must be in the range [0, 1]"
    assert round(w_r + w_g + w_b, 10) == 1, "Weights must sum to 1"

    img_array = np.array(obraz)
    L = img_array[:, :, 0] * w_r + img_array[:, :, 1] * w_g + img_array[:, :, 2] * w_b
    L = np.round(L).astype(np.uint8)
    return Image.fromarray(L, mode='L')

input_image = Image.open("mgla.jpg")

w_r, w_g, w_b = 0.299, 0.587, 0.114

converted_image = konwertuj1(input_image, w_r, w_g, w_b)
converted_image.save("mgla_L1.png")

converted_with_pillow = input_image.convert('L')
converted_with_pillow.save("mgla_L.png")


def konwertuj2(obraz, w_r, w_g, w_b):
    assert 0 <= w_r <= 1 and 0 <= w_g <= 1 and 0 <= w_b <= 1, "Weights must be in the range [0, 1]"
    assert round(w_r + w_g + w_b, 10) == 1, "Weights must sum to 1"

    img_array = np.array(obraz)
    L = img_array[:, :, 0] * w_r + img_array[:, :, 1] * w_g + img_array[:, :, 2] * w_b
    L = np.floor(L).astype(np.uint8)
    return Image.fromarray(L, mode='L')