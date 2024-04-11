import numpy as np
import matplotlib.pyplot as plt

def analytical_reflections(v, z, x):
    Tint = 2.0 * z / v[:-1]
    Vrms = np.zeros(len(z))
    reflections = np.zeros((len(z), len(x)))
    for i in range(len(z)):
        Vrms[i] = np.sqrt(np.sum(v[:i+1]**2 * Tint[:i+1]) / np.sum(Tint[:i+1]))
        reflections[i] = np.sqrt(x**2.0 + 4.0*np.sum(z[:i+1])**2) / Vrms[i]
    return reflections, Vrms

n_receivers = 145
total_time = 0.8

dx = 1
dt = 1e-3

nt = int(total_time / dt) + 1
nx = int(n_receivers / 2) + 1


z = np.array([200, 400])
v = np.array([800, 1200, 2200])

x = np.linspace(0, nx*dx, nx)

reflections, Vrms = analytical_reflections(v, z, x)

plt.figure()
plt.plot(reflections)

plt.show()

print((Vrms))