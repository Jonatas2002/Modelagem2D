import numpy as np
import matplotlib.pyplot as plt

def analytical_reflections(v, z):
    Tint = 2.0 * z / v[:-1]
    Vrms = np.zeros(len(z))
    for i in range(len(z)):
        Vrms[i] = np.sqrt(np.sum(v[:i+1]**2 * Tint[:i+1]) / np.sum(Tint[:i+1]))
    return Vrms

n_receivers = 145
total_time = 0.8

dx = 1
dt = 1e-3

nt = int(total_time / dt) + 1
nx = int(n_receivers / 2) + 1


z = np.array([200, 400])
v = np.array([800, 1200, 2200])

Vrms = analytical_reflections(v, z)

print((Vrms))