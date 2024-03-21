# Importar as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from function import horizon_sin
from function import horizon_gauss
from function import matriz_complexa


"""## Modelo de velocidade 2D """
nx = 4001
nz = 401
dx = 1

depth = np.arange(nz) * dx

# Velocidade e Densidade das camadas
vp = np.array([300, 800, 1200, 2200, 3000])
# Construção da Matriz de Velocidade

#horizon3 = horizon_sin(nz, nx, z0=1.68, height=37.5, L=2.0)
horizon3 = horizon_gauss(nz, nx, z0=10, amplitude=300, desvio=40000)
VP = np.zeros((nz, nx)) + vp[0]
VP = matriz_complexa(nz, nx, VP, horizon3, vp[3])

#-------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------

# Plot dos graficos
plt.figure(figsize=(10,4))
plt.imshow(VP, aspect='auto',extent=(0, nx*dx, nz*dx, 0), cmap='jet')
plt.title('Velocidade P')
#plt.yticks([])  # Remova as marcações do eixo y
plt.xlabel('Distância (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='VP (m/s)')

plt.tight_layout()
plt.show()


