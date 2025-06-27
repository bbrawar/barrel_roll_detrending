import numpy as np
import matplotlib.pyplot as plt

def compute_BRC(time, tec, R=1.0):
    """
    Computes the Barrel-Roll Curve (BRC) for a given TEC time series.
    
    Parameters:
        time (np.array): Array of time values (scaled if needed)
        tec (np.array): Array of TEC values (scaled if needed)
        R (float): Radius of the imaginary barrel (in same units as time axis)
        
    Returns:
        brc_points (np.array): Coordinates (time, tec) of BRC contact points
    """
    contact_times = []
    contact_tecs = []

    i = 0
    N = len(time)

    while i < N:
        x0, y0 = time[i], tec[i]
        contact_times.append(x0)
        contact_tecs.append(y0)

        min_delta = np.inf
        next_i = None

        for j in range(i + 1, N):
            dx = time[j] - x0
            dy = tec[j] - y0
            distance = np.sqrt(dx**2 + dy**2)

            if distance > 2 * R:
                break  # outside barrel range

            # Calculate angular distance delta
            theta = np.arctan2(dy, dx)
            beta = np.arcsin(distance / (2 * R))
            delta_angle = beta - theta

            if delta_angle < min_delta:
                min_delta = delta_angle
                next_i = j

        if next_i is None:
            break

        i = next_i

    return np.array(contact_times), np.array(contact_tecs)

# Example usage with synthetic data
t = np.linspace(0, 10, 1000)
tec = 10 + 0.5 * np.sin(2 * np.pi * t / 3) - np.exp(-((t - 5) ** 2) / 0.2)  # with a depletion

contact_t, contact_tec = compute_BRC(t, tec, R=0.5)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, tec, label='Original TEC')
plt.plot(contact_t, contact_tec, 'r.-', label='Barrel-Roll Curve (BRC)')
plt.xlabel("Time")
plt.ylabel("TEC")
plt.legend()
plt.title("Barrel-Roll Curve (BRC) over TEC Signal")
plt.grid(True)
plt.show()
