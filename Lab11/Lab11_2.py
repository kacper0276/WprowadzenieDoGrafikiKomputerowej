from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
import math

# Zad 1
image1 = Image.open('obraz.png')

image2 = image1.convert('YCbCr')

image2.save('obraz2.jpg')

def rgb_to_ycbcr(image):
    img_np = np.array(image)

    R = img_np[:, :, 0]
    G = img_np[:, :, 1]
    B = img_np[:, :, 2]

    Y = 16 + (64.738 * R + 129.057 * G + 25.064 * B) / 255.
    Cb = 128 + (-37.945 * R - 74.494 * G + 112.439 * B) / 255.
    Cr = 128 + (112.439 * R - 94.154 * G - 18.285 * B) / 255.

    Y = np.round(Y).astype(np.uint8)
    Cb = np.round(Cb).astype(np.uint8)
    Cr = np.round(Cr).astype(np.uint8)

    img_ycbcr = np.stack([Y, Cb, Cr], axis=-1)

    return img_ycbcr

image3_np = rgb_to_ycbcr(image1)

image3 = Image.fromarray(image3_np, mode='YCbCr')

image3.save('obraz3.jpg')

def compare_images(img1, img2):
    np_img1 = np.array(img1)
    np_img2 = np.array(img2)

    diff = np.abs(np_img1 - np_img2)
    total_diff = np.sum(diff)

    different_pixels = np.count_nonzero(diff)

    return total_diff, different_pixels

difference = ImageChops.difference(image2, image3)

difference.save('difference.jpg')

histogram = difference.histogram()

plt.figure(figsize=(10, 6))
plt.bar(range(len(histogram)), histogram, color='blue', alpha=0.7)
plt.title("Histogram różnic między obrazami")
plt.xlabel("Wartość różnicy pikseli (0-255)")
plt.ylabel("Liczba pikseli")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
plt.savefig('histogram.jpg')