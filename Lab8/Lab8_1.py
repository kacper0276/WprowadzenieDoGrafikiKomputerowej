from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt
import numpy as np


def filtruj(obraz, kernel, scale):
    img_array = np.array(obraz.convert("L"))

    kernel = np.array(kernel, dtype=float)

    k_height, k_width = kernel.shape
    assert k_height % 2 == 1 and k_width % 2 == 1, "Kernel musi mieć nieparzyste wymiary."

    pad_h = k_height // 2
    pad_w = k_width // 2

    padded_img = np.pad(img_array, ((pad_h, pad_h), (pad_w, pad_w)), mode="constant", constant_values=0)

    filtered_img = np.zeros_like(img_array, dtype=float)

    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            region = padded_img[i:i + k_height, j:j + k_width]

            filtered_value = np.sum(region * kernel) / scale

            filtered_img[i, j] = np.clip(filtered_value, 0, 255)

    return Image.fromarray(filtered_img.astype("uint8"))


obraz = Image.open("baby_yoda.jpg")
kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

scale = 9

wynik = filtruj(obraz, kernel, scale)

wynik.show()