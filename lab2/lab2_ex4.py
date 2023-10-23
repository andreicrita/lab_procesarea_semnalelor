import numpy as np
import matplotlib.pyplot as plt

amplitudine_sinus = 1.0
frecventa_sinus = 2.0
faza_sinus = 0.0
amplitudine_sawtooth = 0.5
frecventa_sawtooth = 1.0

T = 1.0
ts = 1/1000.0
timp = np.arange(0, T, ts)

semnal_sinus = amplitudine_sinus * np.sin(2 * np.pi * frecventa_sinus * timp + faza_sinus)
semnal_sawtooth = amplitudine_sawtooth * (1 - 2 * (timp * frecventa_sawtooth - np.floor(timp * frecventa_sawtooth + 0.5)))
semnal_suma = semnal_sinus + semnal_sawtooth

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(timp, semnal_sinus)
plt.title('Semnal sinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 2)
plt.plot(timp, semnal_sawtooth)
plt.title('Semnal sawtooth')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 3)
plt.plot(timp, semnal_suma)
plt.title('Suma semnalelor')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
