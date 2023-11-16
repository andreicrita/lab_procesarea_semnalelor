import numpy as np
import matplotlib.pyplot as plt

def fereastra_dreptunghiulara(N):
    return np.ones(N)

def fereastra_hanning(N):
    n = np.arange(N)
    return 0.5 * (1 - np.cos((2 * np.pi * n) / N))

def afiseaza_semnal_cu_fereastra(semnal, fereastra, titlu):
    plt.plot(semnal, label='Semnal Original')
    plt.plot(fereastra, label='Fereastra')
    plt.title(titlu)
    plt.legend()

    plt.tight_layout()

f = 100
A = 1
phi = 0

Nw = 200

t = np.linspace(0, 1, 20000, endpoint=False)
semnal = A * np.sin(2 * np.pi * f * t + phi)

dreptunghiulara = fereastra_dreptunghiulara(Nw)
hanning = fereastra_hanning(Nw)

dreptunghiulara = np.pad(dreptunghiulara, (0, len(t) - len(dreptunghiulara)), 'constant')
hanning = np.pad(hanning, (0, len(t) - len(hanning)), 'constant')

semnal_dreptunghiulara = semnal * dreptunghiulara
semnal_hanning = semnal * hanning

plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
afiseaza_semnal_cu_fereastra(semnal, dreptunghiulara, 'Fereastra Dreptunghiulara')

plt.subplot(3, 1, 2)
afiseaza_semnal_cu_fereastra(semnal, hanning, 'Fereastra Hanning')

plt.subplot(3, 1, 3)
plt.plot(semnal_dreptunghiulara, label='Fereastra Dreptunghiulara')
plt.plot(semnal_hanning, label='Fereastra Hanning')
plt.title('Semnal trecut prin Ferestre')
plt.legend()

plt.tight_layout()
plt.show()
