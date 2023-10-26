import math
import numpy as np
import matplotlib.pyplot as plt

N = 8
matrice_Fourier = np.zeros((N, N), dtype=complex)

for n in range(N):
    for omega in range(N):
        matrice_Fourier[n, omega] = math.e**(-2*math.pi*1j*n*omega/N)

is_unitary = np.allclose(np.conj(matrice_Fourier.T), np.linalg.inv(matrice_Fourier))

print("Matricea Fourier:")
print(matrice_Fourier)

print("\nMatricea Fourier este unitara:", is_unitary)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(matrice_Fourier.real, cmap='coolwarm', vmin=-1, vmax=1)
axs[0].set_title('Partea Reala')
axs[1].imshow(matrice_Fourier.imag, cmap='coolwarm', vmin=-1, vmax=1)
axs[1].set_title('Partea Imaginara')
plt.show()
