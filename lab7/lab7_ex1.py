import numpy as np
import matplotlib.pyplot as plt

N = 512

n1, n2 = np.meshgrid(np.arange(0, N), np.arange(0, N))

# Subpunctul a)
x_a = np.sin(2*np.pi*n1 + 3*np.pi*n2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(x_a, cmap=plt.cm.gray)
plt.title('a) Imaginea pentru x(n1, n2) = sin(2πn1 + 3πn2)')

plt.subplot(1, 2, 2)
Y_a = np.fft.fft2(x_a)
freq_db_a = 20*np.log10(np.abs(np.fft.fftshift(Y_a)))
plt.imshow(freq_db_a)
plt.colorbar()
plt.title('a) Spectrul')

plt.tight_layout()
plt.show()

# Subpunctul b)
x_b = np.sin(4*np.pi*n1) + np.cos(6*np.pi*n2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(x_b, cmap=plt.cm.gray)
plt.title('b) Imaginea pentru x(n1, n2) = sin(4πn1) + cos(6πn2)')

plt.subplot(1, 2, 2)
Y_b = np.fft.fft2(x_b)
freq_db_b = 20*np.log10(np.abs(np.fft.fftshift(Y_b)))
plt.imshow(freq_db_b)
plt.colorbar()
plt.title('b) Spectrul')

plt.tight_layout()
plt.show()

# Subpunctul c)
Y_c = np.zeros_like(n1, dtype=complex)
Y_c[0, 5] = 1
Y_c[0, -5] = 1

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
X_c = np.fft.ifft2(Y_c)
X_c = np.real(X_c)
plt.imshow(X_c, cmap=plt.cm.gray)
plt.title('c) Imaginea pentru Y(0, 5)')

plt.subplot(1, 2, 2)
plt.imshow(20*np.log10(np.abs(np.fft.fftshift(Y_c))))
plt.colorbar()
plt.title('c) Spectrul')

plt.tight_layout()
plt.show()

# Subpunctul d)
Y_d = np.zeros_like(n1, dtype=complex)
Y_d[5, 0] = 1
Y_d[-5, 0] = 1

# Fereastra pentru imaginea și spectrul din d)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
X_d = np.fft.ifft2(Y_d)
X_d = np.real(X_d)
plt.imshow(X_d, cmap=plt.cm.gray)
plt.title('d) Imaginea pentru Y(5,0)')

plt.subplot(1, 2, 2)
plt.imshow(20*np.log10(np.abs(np.fft.fftshift(Y_d))))
plt.colorbar()
plt.title('d) Spectrul')

plt.tight_layout()
plt.show()

# Subpunctul e)
Y_e = np.zeros_like(n1, dtype=complex)
Y_e[5, 5] = 1
Y_e[-5, -5] = 1

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
X_e = np.fft.ifft2(Y_e)
X_e = np.real(X_e)
plt.imshow(X_e, cmap=plt.cm.gray)
plt.title('e) Imaginea pentru Y(5, 5)')

plt.subplot(1, 2, 2)
plt.imshow(20*np.log10(np.abs(np.fft.fftshift(Y_e))))
plt.colorbar()
plt.title('e) Spectrul')

plt.tight_layout()
plt.show()
