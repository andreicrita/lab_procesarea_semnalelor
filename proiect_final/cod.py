from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)

# Adaugam zgomotul
pixel_noise = 200
noise = np.random.randint(-pixel_noise, high=pixel_noise + 1, size=X.shape)
X_noisy = X + noise
X_noisy = np.clip(X_noisy, 0, 255) # ne asiguram ca valorile raman in gama corecta

plt.imshow(X, cmap=plt.cm.gray)
plt.title('Original')
plt.show()

plt.imshow(X_noisy, cmap=plt.cm.gray)
plt.title('Noisy')
plt.show()

snr_before = 10 * np.log10(np.sum(X ** 2) / np.sum(noise ** 2))

# Aplicam filtrul median cu o fereastra mai mare
size_of_median_filter = 5
X_denoised = ndimage.median_filter(X_noisy, size=size_of_median_filter)
X_denoised = np.clip(X_denoised, 0, 255)

plt.imshow(X_denoised, cmap=plt.cm.gray)
plt.title('Denoised')
plt.show()

difference = X - X_denoised
snr_after = 10 * np.log10(np.sum(X ** 2) / np.sum(difference ** 2))

print(f'SNR înainte de denoising: {snr_before:.2f} dB')
print(f'SNR după denoising: {snr_after:.2f} dB')
