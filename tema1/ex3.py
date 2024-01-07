import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from skimage import data, color, img_as_float

imagine = img_as_float(data.astronaut())

imagine_ycbcr = color.rgb2ycbcr(imagine)
canale = [imagine_ycbcr[:, :, i] for i in range(3)]

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

def mse(imagine1, imagine2):
    return np.mean((imagine1 - imagine2) ** 2)

prag_MSE = 0.01

mse_curent = float('inf')
factor_calitate = 1

while mse_curent > prag_MSE:
    imagine_comprimata_ycbcr = np.empty_like(imagine_ycbcr)
    Q_ajustat = Q * factor_calitate

    for canal in range(3):
        h, w = canale[canal].shape
        canal_comprimat = np.zeros((h, w))
        for i in range(0, h - h % 8, 8):
            for j in range(0, w - w % 8, 8):
                bloc = canale[canal][i:i+8, j:j+8]
                bloc_dct = dct2(bloc)
                
                bloc_cuantizat = np.round(bloc_dct / Q_ajustat)
                
                bloc_reconstruit = idct2(bloc_cuantizat * Q_ajustat)
                
                canal_comprimat[i:i+8, j:j+8] = bloc_reconstruit

        imagine_comprimata_ycbcr[:, :, canal] = canal_comprimat

    imagine_comprimata = color.ycbcr2rgb(imagine_comprimata_ycbcr)

    mse_curent = mse(imagine, imagine_comprimata)

    factor_calitate *= 1.1

print("MSE final:", mse_curent)

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(imagine)
plt.title("Imagine originala")
plt.subplot(1, 2, 2)
plt.imshow(imagine_comprimata)
plt.title("Imagine comprimata cu MSE: {:.4f}".format(mse_curent))
plt.show()
