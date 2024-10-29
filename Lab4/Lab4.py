from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zadanie 1

im = Image.open('obrazek.png')

print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)

# Zadanie 2

arrImg = np.array(im)

t_r = arrImg[:, :, 0]
t_g = arrImg[:, :, 1]
t_b = arrImg[:, :, 2]

im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

# im_r.save('obrazek_red.png')
# im_g.save('obrazek_green.png')
# im_b.save('obrazek_blue.png')

im1 = Image.merge('RGB', (im_r, im_g, im_b))

diff = ImageChops.difference(im, im1)


plt.figure(figsize=(16, 16))
plt.subplot(2,2,1)
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(im1)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(diff)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig1.png')
# plt.show()

# Zadanie 3

r, g, b = im.split()

img2 = Image.merge("RGB", (b, g, r))

# img2.save('im2.jpg')
# img2.save('im2.png')

img2Jpg = Image.open('im2.jpg')
img2Png = Image.open('im2.png')

diff2 = ImageChops.difference(img2Jpg, img2Png)

plt.figure(figsize=(16, 16))
plt.subplot(2,2,1)
plt.imshow(img2Jpg)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(img2Png)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(diff2)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig2.png')

# Zadanie 4

obraz = Image.open('beksinski.png')
mix = Image.open('beksinski1.png')

def check_channel_permutation(image1, image2):
    r1, g1, b1 = image1.split()

    if Image.merge('RGB', (r1, g1, b1)) == image2:
        return "No channel change."
    elif Image.merge('RGB', (r1, b1, g1)) == image2:
        return "Channels swapped: G and B."
    elif Image.merge('RGB', (g1, r1, b1)) == image2:
        return "Channels swapped: R and G."
    elif Image.merge('RGB', (g1, b1, r1)) == image2:
        return "Channels swapped: R and B."
    elif Image.merge('RGB', (b1, r1, g1)) == image2:
        return "Channels swapped: R and B, G and R."
    elif Image.merge('RGB', (b1, g1, r1)) == image2:
        return "Channels swapped: R and B, G and B."
    else:
        return "No matching channel permutation found."

def check_negative(image1, image2):
    inverted_image1 = ImageChops.invert(image1)
    return inverted_image1 == image2

def is_negative(original, mix):
    return np.all(mix == 255 - original)

channel_permutation_result = check_channel_permutation(obraz, mix)
print(channel_permutation_result)

if check_negative(obraz, mix):
    print("The mix image is a negative of the original image.")
else:
    print("The mix image is not a negative of the original image.")

# Zadanie 5

def generate_gray_image(width, height):
    gray_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    return Image.fromarray(gray_array, 'L')

im = Image.open('obrazek.png')

im3 = generate_gray_image(im.width, im.height)

def replace_channel(image, gray_image, channel):
    r, g, b = image.split()
    if channel == 'r':
        return Image.merge('RGB', (gray_image, g, b))
    elif channel == 'g':
        return Image.merge('RGB', (r, gray_image, b))
    elif channel == 'b':
        return Image.merge('RGB', (r, g, gray_image))

im_r = replace_channel(im, im3, 'r')
im_g = replace_channel(im, im3, 'g')
im_b = replace_channel(im, im3, 'b')

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(im_r)
axs[0].set_title('Gray in R channel')
axs[1].imshow(im_g)
axs[1].set_title('Gray in G channel')
axs[2].imshow(im_b)
axs[2].set_title('Gray in B channel')

for ax in axs:
    ax.axis('off')

# plt.savefig('fig4.png')
# plt.show()

# Zadanie 6

# im = Image.open('beksinski.png')
#
# plt.hist(np.array(im).ravel(), bins=256, color='gray')
# plt.show()
#
# r, g, b = im.split()
#
# fig, axs = plt.subplots(3, 1, figsize=(10, 8))
#
# axs[0].hist(np.array(r).ravel(), bins=256, color='red')
# axs[0].set_title('Red channel')
#
# axs[1].hist(np.array(g).ravel(), bins=256, color='green')
# axs[1].set_title('Green channel')
#
# axs[2].hist(np.array(b).ravel(), bins=256, color='blue')
# axs[2].set_title('Blue channel')
#
# plt.tight_layout()
# plt.show()
#
# pixels_with_value_1 = np.sum(np.array(g) == 1)
# print(f"Liczba pikseli o wartości 1 w kanale zielonym: {pixels_with_value_1}")

im = Image.open('beksinski.png')

hist = obraz.histogram()

# Kanał czerwony
plt.figure()
plt.title("Histogram - Kanał Czerwony")
plt.bar(range(256), hist[:256], color='r', alpha=0.7)
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
# plt.show()

# Kanał zielony
plt.figure()
plt.title("Histogram - Kanał Zielony")
plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.7)
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
# plt.show()

# Kanał niebieski
plt.figure()
plt.title("Histogram - Kanał Niebieski")
plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.7)
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
# plt.show()

wartosc = 1
kanal = 'g'

obraz_array = np.array(obraz)
kanal_map = {'r': 0, 'g': 1, 'b': 2}
indeks_kanalu = kanal_map[kanal]

wybrany_kanal = obraz_array[:, :, indeks_kanalu]
liczba_pikseli = np.sum(wybrany_kanal == wartosc)

print(f"Liczba pikseli o wartości {wartosc} na kanale {kanal.upper()}: {liczba_pikseli}")

# Zadanie 7

def are_images_identical(im1, im2):
    if im1.mode != im2.mode or im1.size != im2.size:
        return False
    diff = ImageChops.difference(im1, im2)
    return not diff.getbbox()

im1 = Image.open('obrazek.png')
im2 = Image.open('beksinski.png')

if are_images_identical(im1, im2):
    print("Obrazy są identyczne")
else:
    print("Obrazy są różne")

diff = ImageChops.difference(im1, im2)

amplified_diff = diff.point(lambda x: x * 10)

# amplified_diff.show()