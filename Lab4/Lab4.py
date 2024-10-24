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

print(diff)