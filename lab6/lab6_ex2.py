import numpy as np
import matplotlib.pyplot as plt

def genereaza_polinom(N):
    return np.random.randint(-10, 11, N + 1)

N = 5

coef_p = genereaza_polinom(N)
coef_q = genereaza_polinom(N)

print(f"p(x): {coef_p}")
print(f"q(x): {coef_q}")

# Calculam produsul utilizand convolutia directa
rez_convolutie = np.convolve(coef_p, coef_q, mode='full')

print(f"Produsul folosind convolutia directa: {rez_convolutie}")

# Calculam produsul utilizand inmultirea directa a polinoamelor
rez_inmultire = np.polymul(coef_p, coef_q)

print(f"Produsul folosind inmultirea directa a polinoamelor: {rez_inmultire}")

# Calculam produsul utilizând FFT
rez_fft = np.fft.ifft(np.fft.fft(coef_p) * np.fft.fft(coef_q)).real

print(f"Produsul folosind FFT: {rez_fft}")

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(coef_p, label='p(x)')
plt.legend()

plt.subplot(2, 2, 2)
plt.stem(coef_q, label='q(x)')
plt.legend()

plt.subplot(2, 2, 3)
plt.stem(rez_convolutie, label='Convolutia Directa')
plt.legend()

plt.subplot(2, 2, 4)
plt.stem(rez_fft, label='FFT')
plt.legend()

plt.show()
