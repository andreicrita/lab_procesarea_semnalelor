from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)

pixel_noise = 200
noise = np.random.randint(-pixel_noise, high=pixel_noise + 1, size=X.shape)
X_noisy = X + noise

plt.imshow(X, cmap=plt.cm.gray)
plt.title('Original')
plt.show()

plt.imshow(X_noisy, cmap=plt.cm.gray)
plt.title('Noisy')
plt.show()

snr_before = 10 * np.log10(np.sum(X ** 2) / np.sum(noise ** 2))

X_denoised = np.median(X_noisy)

snr_after = 10 * np.log10(np.sum(X ** 2) / np.sum((X - X_denoised) ** 2))

plt.imshow(X_denoised, cmap=plt.cm.gray)
plt.title('Denoised')
plt.show()

print(f'SNR înainte de denoising: {snr_before:.2f} dB')
print(f'SNR după denoising: {snr_after:.2f} dB')
