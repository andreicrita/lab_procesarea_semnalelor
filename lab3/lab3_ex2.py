import numpy as np
import matplotlib.pyplot as plt

frecventa = 7
rata_esantionare = 10 * frecventa

t = np.arange(0, 1, 1/rata_esantionare)
x = np.sin(2 * np.pi * frecventa * t)

n = np.arange(len(x))
y = x * np.exp(-2j * np.pi * n / len(x))

distance = np.abs(y)

colors = distance / np.max(distance)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x, color='blue')
plt.title('Semnal Sinusoidal')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')

plt.axhline(0, color='black', linewidth=0.5, linestyle='-')

plt.subplot(1, 2, 2)
plt.scatter(y.real, y.imag, c=colors, cmap='viridis')
plt.title('Infasurarea pe Cercul Unitate')
plt.xlabel('Partea Reală')
plt.ylabel('Partea Imaginară')
plt.colorbar(label='Distanța de la Origine')

plt.axhline(0, color='black', linewidth=0.5, linestyle='-')
plt.axvline(0, color='black', linewidth=0.5, linestyle='-')

plt.show()
