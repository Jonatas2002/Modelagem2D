# Testando os modelos em tempo
import numpy as np
import matplotlib.pyplot as plt
from function import model_1D
from function import model_paralelo_2D

nx = 501
nz = 501
dx = 1
time = 1
dt = time/nz

# Teste 1D modelo no tempo
t = np.arange(nz) * dt

tempo = np.array([0.2, 0.4, 0.6, 0.8, 1])
vp = np.array([300, 800, 1200, 2200, 3000])

VP = model_1D(nz, dt, tempo, vp)

plt.figure(figsize=(3,7))
plt.plot(VP, t)
plt.ylim(max(t),min(t))
plt.show()

# Testando modelo 2D no tempo
VP_2D = model_paralelo_2D(nz, nx, dt, tempo, vp)

plt.figure()
plt.title('VP (m/s)')
plt.imshow(VP_2D, aspect='auto', extent= (0, nx*dx, nz*dt, 0), cmap='jet')
plt.xlabel('Distâcia (m)')
plt.ylabel('Tempo (s)')

plt.show()
