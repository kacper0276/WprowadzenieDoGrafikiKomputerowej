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