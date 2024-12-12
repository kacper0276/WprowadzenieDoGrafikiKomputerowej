from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad 1
obraz = Image.open("zeby.png").convert("L")

