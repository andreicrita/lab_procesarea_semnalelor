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

def exponential_smoothing(series, alpha):
    result = np.cumsum(series * alpha) / np.arange(1, len(series) + 1)
    return result

N = 1000
time_series, _, _, _, _ = generate_time_series(N)

alpha_fixed = 0.1

smoothed_series_fixed = exponential_smoothing(time_series, alpha_fixed)

plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Seria de timp originala')
plt.plot(smoothed_series_fixed, label=f'Seria mediata exponential (α={alpha_fixed})')
plt.title('Seria de timp originala si seria mediata exponential')
plt.legend()
plt.show()

alphas = np.linspace(0.01, 1, 100)
mse_values = []

for alpha in alphas:
    smoothed_series = exponential_smoothing(time_series, alpha)
    mse = np.mean((time_series - smoothed_series)**2)
    mse_values.append(mse)

optimal_alpha = alphas[np.argmin(mse_values)]

smoothed_series_optimal = exponential_smoothing(time_series, optimal_alpha)

plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Seria de timp originala')
plt.plot(smoothed_series_optimal, label=f'Seria mediata exponential (α={optimal_alpha:.2f} - optim)')
plt.title('Seria de timp originala si seria mediata exponential (α optim)')
plt.legend()
plt.show()

print(f'α optim: {optimal_alpha:.2f}')
