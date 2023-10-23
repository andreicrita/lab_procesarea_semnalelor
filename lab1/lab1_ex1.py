import numpy as np
import matplotlib.pyplot as plt

fs = 200
t = np.arange(0, 0.03, 0.0005)

x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

fig, axs = plt.subplots(3)
fig.suptitle('Semnale continue')

axs[0].plot(t, x)
axs[1].plot(t, y)
axs[2].plot(t, z)

for ax in axs.flat:
    ax.set_xlim([0, 0.03])
    ax.set_xlabel('Timp')
    ax.set_ylabel('Amplitudine')

axs[0].stem(t, x)
axs[1].stem(t, y)
axs[2].stem(t, z)

plt.tight_layout()
plt.show()