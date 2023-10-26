import numpy as np
import matplotlib.pyplot as plt

rata_esantionare = 100
durata = 1.0
t = np.linspace(0, durata, int(rata_esantionare * durata), endpoint=False)

frecvente = [5, 10, 20]

semnal = np.sum([np.sin(2 * np.pi * f * t) for f in frecvente], axis=0)

N = len(semnal)
fourier = np.fft.fft(semnal)
frecvente = np.fft.fftfreq(N, 1 / rata_esantionare)
amplitudini = np.abs(fourier)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, semnal, color='blue')
plt.title('Semnal Compus')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')

plt.subplot(1, 2, 2)
plt.plot(frecvente, amplitudini, color='green')
plt.title('Transformata Fourier')
plt.xlabel('Frecventa (Hz)')
plt.ylabel('Amplitudine')

plt.show()
