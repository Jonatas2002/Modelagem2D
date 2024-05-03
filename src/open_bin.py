import numpy as np
import matplotlib.pyplot as plt


# Leitura do arquivo
nx = 4001
nz = 401
dx = 1

VP = np.reshape(np.fromfile("vp_2D_401x4001_1m.bin", dtype=np.float32), (nx, nz))
VS = np.reshape(np.fromfile("vs_2D_401x4001_1m.bin", dtype=np.float32), (nx, nz))
RHOB = np.reshape(np.fromfile("rhob_2D_401x4001_1m.bin", dtype=np.float32), (nx, nz))


# Plotando o modelo de velocidade
plt.figure()
plt.title('Velocity Model')
plt.imshow(VP.T, aspect='auto', cmap='Grays', extent=[0, nx * dx, nz * dx, 0])
plt.xlabel('Distance [m]')
plt.ylabel('Depth [m]')
plt.colorbar(label='VS (m/s)')
plt.show()

plt.figure()
plt.title('VS (m/s)')
plt.imshow(VS.T, aspect='auto', extent= (0, nx*dx, nz*dx, 0),  cmap='Grays')
plt.xlabel('Distâcia (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='VS (m/s)')
plt.show()


plt.figure()
plt.title('RHOB (kg/m³)')
plt.imshow(RHOB.T, aspect='auto', extent= (0, nx*dx, nz*dx, 0), cmap='Grays')
plt.xlabel('Distâcia (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='RHOB (Kg/m³)')
plt.show()
