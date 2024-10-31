from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad 1
im = Image.open('obrazek.png')

r, g, b = im.split()
im2 = Image.merge("RGB", (g, r, b))

im2.save("test/im2.jpg")
im2.save("test/im2.png")

im2_jpg = Image.open("test/im2.jpg")
im2_png = Image.open("test/im2.png")

diff = ImageChops.difference(im2_jpg, im2_png)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(im2_jpg)
axs[0].set_title("im2.jpg")
axs[0].axis("off")

axs[1].imshow(im2_png)
axs[1].set_title("im2.png")
axs[1].axis("off")

axs[2].imshow(diff)
axs[2].set_title("Difference (im2.jpg vs im2.png)")
axs[2].axis("off")

plt.savefig("test/fig2.png")

plt.show()

#  Zad 2
def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)
    print("count ", s.count)
    print("mean ", s.mean)
    print("median ", s.median)
    print("stddev ", s.stddev)

im = Image.open('./test/obraz10.jpg')

statystyki(im)

im_array = np.array(im)

std_r = np.std(im_array[:, :, 0])
std_g = np.std(im_array[:, :, 1])
std_b = np.std(im_array[:, :, 2])

std_r = round(std_r, 1)
std_g = round(std_g, 1)
std_b = round(std_b, 1)

print(f"{std_r} {std_g} {std_b}")

# Zad 3
def sprawdz_typ_mix(obraz_org_path, obraz_mix_path):
    obraz_org = Image.open(obraz_org_path)
    obraz_mix = Image.open(obraz_mix_path)

    negatyw = ImageChops.invert(obraz_org)
    if ImageChops.difference(negatyw, obraz_mix).getbbox() is None:
        return "mix29.png jest negatywem obraz9.jpg"

    r, g, b = obraz_org.split()

    permutacje = {
        "GRB": Image.merge("RGB", (g, r, b)),
        "BRG": Image.merge("RGB", (b, r, g)),
        "BGR": Image.merge("RGB", (b, g, r)),
        "GBR": Image.merge("RGB", (g, b, r)),
        "RBG": Image.merge("RGB", (r, b, g))
    }

    for nazwa, permutowany in permutacje.items():
        if ImageChops.difference(permutowany, obraz_mix).getbbox() is None:
            return f"mix29.png powstał przez permutację kanałów: {nazwa}"

    return "mix29.png nie jest ani negatywem, ani permutacją kanałów obraz9.jpg"

wynik = sprawdz_typ_mix('./test/obraz9.jpg', './test/mix29.png')
print(wynik)

# Zad 4
im = Image.open('./test/obraz11.jpg')

zielony_kanal = im.split()[1]

zielony_array = np.array(zielony_kanal)

hist = zielony_kanal.histogram()

liczba_pikseli_50 = hist[50]

plt.figure(figsize=(8, 6))
plt.bar(range(256), hist, color='green', alpha=0.7)
plt.title("Histogram Zielonego Kanału")
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
plt.grid(True)

plt.savefig('kolos/hist.png')

print(liczba_pikseli_50)

# Zad 5
def are_images_identical(img1, img2):
    if img1.size != img2.size or img1.mode != img2.mode:
        return False

    roznica = ImageChops.difference(img1, img2)

    roznica_np = np.array(roznica)

    return np.all(roznica_np == 0)

im1 = Image.open('./test/mix29.png')
im2 = Image.open('./test/obraz10.jpg')

if are_images_identical(im1, im2):
    print("Obrazy są identyczne")
else:
    print("Obrazy są różne")

# Zad 6
def highlight_differences(img1, img2):
    if img1.size != img2.size or img1.mode != img2.mode:
        return None

    roznica = ImageChops.difference(img1, img2)

    highlighted = img1.copy()

    red_color = (255, 0, 0)

    for x in range(roznica.width):
        for y in range(roznica.height):
            pixel_difference = roznica.getpixel((x, y))
            print(pixel_difference)

            if pixel_difference[0] != 0 or pixel_difference[1] != 0 or pixel_difference[2] != 0:
                highlighted.putpixel((x, y), red_color)

    return highlighted

highlighted_image = highlight_differences(im1, im2)
if highlighted_image is not None:
        highlighted_image.show()

im = Image.open('obrazek.png')

t_r, t_g, t_b = im.split()
im_r = t_r
im_g = t_g
im_b = t_b

im1 = Image.merge("RGB", (im_r, im_g, im_b))

im1.save('kolos/im1.png')
im.save('kolos/im.png')

roznica = ImageChops.difference(im, im1)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Oryginalny obraz")
plt.imshow(im)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Obraz po scaleniu kanałów")
plt.imshow(im1)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Różnica między obrazami")
plt.imshow(roznica)
plt.axis("off")

plt.savefig("kolos/fig1.png")
plt.show()

# Zad 7
def szary(w, h):
    gray_image = np.zeros((h, w), dtype=np.uint8)
    for j in range(h):
        for i in range(w):
            gray_image[j, i] = (i + 3 * j) % 256
    return Image.fromarray(gray_image, 'L')

obraz = Image.open('./test/obraz9.jpg')

w, h = obraz.size
szary_obraz = szary(w, h)

r, g, b = obraz.split()
obraz_wynikowy = Image.merge("RGB", (szary_obraz, g, b))

obraz_wynikowy.save("kolos/mix.png")