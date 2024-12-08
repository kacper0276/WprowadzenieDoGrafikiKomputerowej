from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt
import numpy as np

# Zad 1

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

# wynik.show()

# Zad 2
def statystyki_obrazu(obr):
    obr_array = np.array(obr)
    return {
        "Średnia": np.mean(obr_array),
        "Odchylenie standardowe": np.std(obr_array),
        "Minimum": np.min(obr_array),
        "Maksimum": np.max(obr_array),
    }

blur_pil = obraz.filter(ImageFilter.BLUR)

kernel_blur = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
scale_blur = 9
blur_custom = filtruj(obraz, kernel_blur, scale_blur)

roznica = ImageChops.difference(blur_pil.convert("L"), blur_custom.convert("L"))

statystyki = statystyki_obrazu(roznica)

fig, axs = plt.subplots(1, 4, figsize=(20, 5))

axs[0].imshow(obraz, cmap="gray")
axs[0].set_title("Obraz oryginalny")
axs[0].axis("off")

axs[1].imshow(blur_pil, cmap="gray")
axs[1].set_title("ImageFilter.BLUR")
axs[1].axis("off")

axs[2].imshow(blur_custom, cmap="gray")
axs[2].set_title("Filtr własny")
axs[2].axis("off")

axs[3].imshow(roznica, cmap="gray")
axs[3].set_title("Różnica obrazów")
axs[3].axis("off")

plt.tight_layout()
plt.savefig("fig1.png")
plt.show()
