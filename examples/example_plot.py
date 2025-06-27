import numpy as np
import matplotlib.pyplot as plt
import datetime
from brc import compute_BRC

# Example with datetime x-axis
t = np.array([np.datetime64('2020-01-01T00:00') + np.timedelta64(int(600 * i), 's') for i in range(1000)])
t_seconds = (t - t[0]) / np.timedelta64(1, 's')
tec = 10 + 0.5 * np.sin(2 * np.pi * t_seconds / 1800) - np.exp(-((t_seconds - 3000) ** 2) / 200)

contact_t, contact_tec = compute_BRC(t, tec, R=500)

plt.figure(figsize=(10, 5))
plt.plot(t, tec, label='Original TEC')
plt.plot(contact_t, contact_tec, 'r.-', label='Barrel-Roll Curve (BRC)')
plt.xlabel("Time")
plt.ylabel("TEC")
plt.legend()
plt.title("Barrel-Roll Curve (BRC) over TEC Signal (Datetime Axis)")
plt.grid(True)
plt.tight_layout()
plt.show()
