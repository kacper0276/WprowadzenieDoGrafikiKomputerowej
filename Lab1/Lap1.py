from PIL import Image
import numpy as np

# Wczytanie obrazu
obrazek = Image.open('inicjaly.bmp')
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# Wczytanie danych do obrazu
dane_obrazka = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile bajtów trzeba do zapisu wartości elementu
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])
print("***************************************")
print(dane_obrazka)

# obrazek.show() - wyświetlenie obrazka

# Zapis tablicy do pliku
f1_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        f1_text.write(str(int(item)) + ' ')
    f1_text.write('\n')

f1_text.close()

# Odczyt danych z pliku
t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
t2 = np.loadtxt("inicjaly.txt", dtype=np.int_)
t3 = np.loadtxt("inicjaly.txt", dtype=np.uint8)

# w zależnosci od tego, jakie operacje chcemy zrobić na tablicy, wybieramy jedną z powyższych postaci tablicy
print("typ danych tablicy t1:", t1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t1 :", t1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t1 :", t1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("typ danych tablicy t2:", t2.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t2 :", t2.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t2 :", t2.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("typ danych tablicy t3:", t3.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t3 :", t3.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t3 :", t3.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

ob_d = Image.fromarray(t3)
ob_d.show()