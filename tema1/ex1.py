import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from scipy import fftpack

imagine = datasets.ascent()

Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

def dct2(bloc):
    return fftpack.dct(fftpack.dct(bloc.T, norm='ortho').T, norm='ortho')

def idct2(bloc):
    return fftpack.idct(fftpack.idct(bloc.T, norm='ortho').T, norm='ortho')

h, w = imagine.shape
imagine_comprimata = np.zeros(imagine.shape)

for i in range(0, h - h % 8, 8):
    for j in range(0, w - w % 8, 8):
        bloc = imagine[i:i+8, j:j+8]
        bloc_dct = dct2(bloc)
        
        bloc_cuantizat = np.round(bloc_dct / Q)
        
        bloc_reconstruit = idct2(bloc_cuantizat * Q)
        
        imagine_comprimata[i:i+8, j:j+8] = bloc_reconstruit

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagine, cmap=plt.cm.gray)
plt.title("Imagine originala")

plt.subplot(1, 2, 2)
plt.imshow(imagine_comprimata, cmap=plt.cm.gray)
plt.title("Imagine comprimat")
plt.show()
