import numpy as np
import matplotlib.pyplot as plt

def generate_time_series(N):
    np.random.seed(42)
    time = np.arange(N)
    trend = 0.02 * time**2
    season1 = 10 * np.sin(0.02 * time)
    season2 = 5 * np.sin(0.05 * time)
    noise = np.random.normal(0, 1, N)
    time_series = trend + season1 + season2 + noise
    return time_series

N = 1000

time_series = generate_time_series(N)

autocorr = np.correlate(time_series, time_series, mode='full')

autocorr /= np.max(autocorr)

plt.figure(figsize=(12, 6))
plt.plot(autocorr)
plt.title('Vectorul de autocorelatie')
plt.xlabel('Intarziere temporala')
plt.ylabel('Autocorelatie normalizata')
plt.grid(True)
plt.show()
