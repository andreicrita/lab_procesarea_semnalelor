import numpy as np
import matplotlib.pyplot as plt

# (a) Semnal sinusoidal de 400 Hz cu 1600 de esantioane
fs = 100
t = np.arange(0, 1, 1/fs)
signal_a = np.sin(2 * np.pi * 400 * t)

plt.figure(1)
plt.subplot(411)
plt.plot(t, signal_a)
plt.title('Semnal sinusoidal 400 Hz')

# (b) Semnal sinusoidal de 800 Hz cu o durata de 3 secunde
fs_b = 100
t_b = np.arange(0, 3, 1/fs_b)
signal_b = np.sin(2 * np.pi * 800 * t_b)

plt.subplot(412)
plt.plot(t_b, signal_b)
plt.title('Semnal sinusoidal 800 Hz')

# (c) Semnal de tip sawtooth de 240 Hz
t_c = np.arange(0, 1, 1/fs)
signal_c = 2 * (t_c * 240 - np.floor(t_c * 240 + 0.5))

plt.subplot(413)
plt.plot(t_c, signal_c)
plt.title('Semnal sawtooth 240 Hz')

# (d) Semnal de tip square de 300 Hz
t_d = np.arange(0, 1, 1/fs)
signal_d = np.sign(np.sin(2 * np.pi * 300 * t_d))

plt.subplot(414)
plt.plot(t_d, signal_d)
plt.title('Semnal square 300 Hz')

plt.tight_layout()
plt.show()
