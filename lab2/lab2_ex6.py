import numpy as np
import matplotlib.pyplot as plt

fs = 300

timp = np.arange(0, 1, 1/fs)

# (a) frecventa f = fs/2
frecventa_a = fs / 2
semnal_a = np.sin(2 * np.pi * frecventa_a * timp)

# (b) frecventa f = fs/4
frecventa_b = fs / 4
semnal_b = np.sin(2 * np.pi * frecventa_b * timp)

# (c) frecventa f = 0 Hz
frecventa_c = 0
semnal_c = np.sin(2 * np.pi * frecventa_c * timp)

plt.figure(figsize=(10, 6))

# Subplot pentru semnalul (a)
plt.subplot(3, 1, 1)
plt.plot(timp, semnal_a)
plt.title('Semnal cu f = fs/2')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

# Subplot pentru semnalul (b)
plt.subplot(3, 1, 2)
plt.plot(timp, semnal_b)
plt.title('Semnal cu f = fs/4')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

# Subplot pentru semnalul (c)
plt.subplot(3, 1, 3)
plt.plot(timp, semnal_c)
plt.title('Semnal cu f = 0 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
