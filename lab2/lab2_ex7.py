import numpy as np
import matplotlib.pyplot as plt

fs = 300

timp = np.arange(0, 1, 1/fs)

frecventa = 100  # Hz
semnal_original = np.sin(2 * np.pi * frecventa * timp)

# (a) Decimare incepand de la primul element al vectorului
semnal_decimat_a = semnal_original[::4]

# (b) Decimare incepand de la al doilea element al vectorului
semnal_decimat_b = semnal_original[1::4]

plt.figure(figsize=(10, 6))

# Subplot pentru semnalul original
plt.subplot(3, 1, 1)
plt.plot(timp, semnal_original)
plt.title('Semnal original')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

# Subplot pentru semnalul decimat (a)
timp_decimat_a = np.arange(0, len(semnal_decimat_a) * (1/fs), 1/fs)
plt.subplot(3, 1, 2)
plt.plot(timp_decimat_a, semnal_decimat_a)
plt.title('Semnal decimat (a)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

# Subplot pentru semnalul decimat (b)
timp_decimat_b = np.arange(0, len(semnal_decimat_b) * (1/fs), 1/fs)
plt.subplot(3, 1, 3)
plt.plot(timp_decimat_b, semnal_decimat_b)
plt.title('Semnal decimat (b)')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()


#  (a) Cand decimam incepand de la primul element al vectorului, semnalul decimat (a) are aceeasi faza cu semnalul original, dar frecvența sa este de 1/4 din frecventa initiala. Se observa o redresare evidenta a semnalului.
#  (b) Cand decimam incepand de la al doilea element al vectorului, semnalul decimat (b) are o faza initiala diferita, deoarece pornim de la al doilea esantion. Acest lucru duce la o schimbare in faza in comparatie cu semnalul original.