from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)

plt.imshow(X, cmap=plt.cm.gray)
plt.show()

Y = np.fft.fft2(X)
freq_db = 20 * np.log10(np.abs(Y))

freq_cutoff = 120

Y_cutoff = Y.copy()
Y_cutoff[freq_db > freq_cutoff] = 0

X_cutoff = np.fft.ifft2(Y_cutoff)
X_cutoff = np.real(X_cutoff)

plt.imshow(X_cutoff, cmap=plt.cm.gray)
plt.show()
