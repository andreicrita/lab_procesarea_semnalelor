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

    return time_series, trend, season1, season2, noise

N = 1000

time_series, trend, season1, season2, noise = generate_time_series(N)

plt.figure(figsize=(12, 6))

plt.subplot(4, 1, 1)
plt.plot(time_series, label='Seria de timp totala')
plt.title('Seria de timp totala')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(trend, label='Trend')
plt.title('Componenta de trend')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(season1, label='Sezon 1')
plt.plot(season2, label='Sezon 2')
plt.title('Componenta de sezon')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(noise, label='Zgomot')
plt.title('Variatii mici (Zgomot)')
plt.legend()

plt.tight_layout()
plt.show()
