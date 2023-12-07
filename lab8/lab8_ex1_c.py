import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

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

p = 10

model = sm.tsa.AutoReg(time_series, lags=p)
results = model.fit()

predictions = results.predict(start=p, end=N-1)

plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Seria de timp originala')
plt.plot(predictions, label='Predicții AR')
plt.title('Seria de timp originala si predictiile AR')
plt.legend()
plt.show()
