# Importar as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

from function import horizon_cos
from function import horizon_sin
from function import matriz_complexa
from function import matriz_falha
from function import horizon_reta

"""## Modelo de velocidade 2D """
nx = 501
nz = 501
dx = 1

depth = np.arange(nz) * dx

# Velocidade e Densidade das camadas
vel = np.array([1500, 4000, 2000, 4500, 5000, 7000])  # Velocidade

# Construção da Matriz de Velocidade
velocidade = np.zeros((nz, nx)) + vel[0]

#horizon1 = horizon_reta(nx, a=5, b=1)
horizon1 = horizon_cos(nz, nx, z0=3.00, height=60, L=2.0)
horizon2 = horizon_cos(nz, nx, z0=2.50, height=90, L=2.0)
horizon3 = horizon_sin(nz, nx, z0=1.45, height=70, L=1.8)
horizon4 = horizon_sin(nz, nx, z0=1.00, height=90, L=1.9)
horizon41 = horizon_sin(nz, nx, z0=1.05, height=90, L=1.9)
horizon5 = horizon_sin(nz, nx, z0=1.00, height=170, L=8.0)


velocidade = matriz_complexa(nz, nx, velocidade, horizon1, vel[1])
velocidade = matriz_complexa(nz, nx, velocidade, horizon2, vel[2])
velocidade = matriz_complexa(nz, nx, velocidade, horizon3, vel[3])
velocidade = matriz_complexa(nz, nx, velocidade, horizon4, vel[4])
velocidade = matriz_falha(nz, nx, velocidade, horizon4, vel[4], If=60, Ff=90)
velocidade = matriz_complexa(nz, nx, velocidade, horizon5, vel[5])

#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#

# Plot dos graficos
plt.figure(figsize=(15,10))
plt.imshow(velocidade, aspect='auto',
           extent=(0, nx*dx, nz*dx, 0), cmap='jet')
plt.title('Velocidade')
#plt.yticks([])  # Remova as marcações do eixo y
plt.xlabel('Distância (m)')
plt.ylabel('Profundidade (M)')

plt.show()
