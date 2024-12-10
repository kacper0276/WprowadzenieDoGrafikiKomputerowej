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

wynik.show()

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

# Zad 3
emboss_pil = obraz.filter(ImageFilter.EMBOSS)

kernel_sobel1 = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1]).reshape((3, 3))
kernel_sobel2 = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1]).reshape((3, 3))

sobel1_img = filtruj(obraz, kernel_sobel1, scale=1)
sobel2_img = filtruj(obraz, kernel_sobel2, scale=1)

fig, axs = plt.subplots(1, 4, figsize=(20, 5))

axs[0].imshow(obraz, cmap="gray")
axs[0].set_title("Obraz w skali szarości (L)")
axs[0].axis("off")

axs[1].imshow(emboss_pil, cmap="gray")
axs[1].set_title("Filtr EMBOSS")
axs[1].axis("off")

axs[2].imshow(sobel1_img, cmap="gray")
axs[2].set_title("Filtr SOBEL1")
axs[2].axis("off")

axs[3].imshow(sobel2_img, cmap="gray")
axs[3].set_title("Filtr SOBEL2")
axs[3].axis("off")

plt.tight_layout()
plt.savefig("fig2.png")
# plt.show()

# Zad 4
filters = [ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.SHARPEN, ImageFilter.SMOOTH_MORE]
filter_names = ["DETAIL", "EDGE_ENHANCE_MORE", "SHARPEN", "SMOOTH_MORE"]

fig, axs = plt.subplots(len(filters), 2, figsize=(10, 15))

for i, (filt, name) in enumerate(zip(filters, filter_names)):
    filtered_img = obraz.filter(filt)
    diff_img = ImageChops.difference(obraz, filtered_img)

    axs[i, 0].imshow(filtered_img, cmap="gray")
    axs[i, 0].set_title(f"Filtr: {name}")
    axs[i, 0].axis("off")

    axs[i, 1].imshow(diff_img, cmap="gray")
    axs[i, 1].set_title(f"Różnica: {name}")
    axs[i, 1].axis("off")

plt.tight_layout()
plt.savefig("fig3.png")

# Zadanie 5
filters_with_params = [
    (ImageFilter.GaussianBlur(radius=2), "GaussianBlur (radius=2)"),
    (ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3), "UnsharpMask (r=2, p=150, t=3)"),
    (ImageFilter.MedianFilter(size=3), "MedianFilter (size=3)"),
    (ImageFilter.MinFilter(), "MinFilter"),
    (ImageFilter.MaxFilter(), "MaxFilter"),
]

fig, axs = plt.subplots(len(filters_with_params), 2, figsize=(10, 20))

for i, (filt, name) in enumerate(filters_with_params):
    filtered_img = obraz.filter(filt)
    diff_img = ImageChops.difference(obraz, filtered_img)

    axs[i, 0].imshow(filtered_img, cmap="gray")
    axs[i, 0].set_title(f"Filtr: {name}")
    axs[i, 0].axis("off")

    axs[i, 1].imshow(diff_img, cmap="gray")
    axs[i, 1].set_title(f"Różnica: {name}")
    axs[i, 1].axis("off")

plt.tight_layout()
plt.savefig("fig4.png")
