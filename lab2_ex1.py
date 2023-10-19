import numpy as np
import matplotlib.pyplot as plt


amplitudine = 1.0
frecventa = 2.0
faza = 0.0

timp = np.linspace(0, 2 * np.pi, 1000)
semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)
semnal_cosinus = amplitudine * np.cos(2 * np.pi * frecventa * timp + faza)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(timp, semnal_sinus)
plt.title("Semnal Sinusoidal")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")

plt.subplot(2, 1, 2)
plt.plot(timp, semnal_cosinus)
plt.title("Semnal Cosinusoidal")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")

plt.tight_layout()
plt.show()
