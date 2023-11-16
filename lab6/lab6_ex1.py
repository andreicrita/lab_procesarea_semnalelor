import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.rand(N)

for _ in range(3):
    x = np.convolve(x, x, mode='full')

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x)
plt.title('Vectorul Generat')

for i in range(2, 5):
    x = np.convolve(x, x, mode='full')
    plt.subplot(2, 2, i)
    plt.plot(x)
    plt.title(f'Convolutia #{i-1}')

plt.show()
