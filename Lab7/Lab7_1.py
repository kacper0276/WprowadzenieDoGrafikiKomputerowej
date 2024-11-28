from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)

    max_vals = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            max_vals[0] = max(max_vals[0], pixel[0])
            max_vals[1] = max(max_vals[1], pixel[1])
            max_vals[2] = max(max_vals[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (max_vals[0], max_vals[1], max_vals[2])

    return obraz1

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)

    min_vals = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            min_vals[0] = min(min_vals[0], pixel[0])
            min_vals[1] = min(min_vals[1], pixel[1])
            min_vals[2] = min(min_vals[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (min_vals[0], min_vals[1], min_vals[2])

    return obraz1