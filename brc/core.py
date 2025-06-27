import numpy as np
import datetime

def compute_BRC(time, tec, R=1.0):
    """
    Computes the Barrel-Roll Curve (BRC) for a given TEC time series.

    Parameters:
        time (np.ndarray): 1D array of time values (numeric or datetime64)
        tec (np.ndarray): 1D array of TEC values
        R (float): Radius of the imaginary barrel (in same units as time axis)

    Returns:
        tuple: (brc_times, brc_tec), arrays of contact point times and TECs
    """
    if isinstance(time[0], (np.datetime64, datetime.datetime)):
        time = np.array((time - time[0]) / np.timedelta64(1, 's'), dtype=float)
        datetime_mode = True
    else:
        time = np.asarray(time, dtype=float)
        datetime_mode = False

    tec = np.asarray(tec, dtype=float)
    
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
            distance = np.hypot(dx, dy)

            if distance > 2 * R:
                break

            theta = np.arctan2(dy, dx)
            try:
                beta = np.arcsin(distance / (2 * R))
            except ValueError:
                continue  # numerical instability if slightly >1 due to float precision

            delta_angle = beta - theta

            if delta_angle < min_delta:
                min_delta = delta_angle
                next_i = j

        if next_i is None:
            break

        i = next_i

    brc_times = np.array(contact_times)
    if datetime_mode:
        brc_times = np.array([np.datetime64(int(t * 1e9), 'ns') + np.datetime64('1970-01-01T00:00:00Z') for t in brc_times])
    
    return brc_times, np.array(contact_tecs)
