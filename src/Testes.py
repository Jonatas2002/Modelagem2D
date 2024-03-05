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
dx = 2

depth = np.arange(nz) * dx

# Velocidade e Densidade das camadas
vel = np.array([1500, 4000, 2000, 4500, 5000, 7000])  # Velocidade

"""# Construção da Matriz de Velocidade e
velocidade = np.zeros((nz, nx)) + vel[0]

horizon1 = np.zeros(nx,dtype='int')
horizon2 = np.zeros(nx,dtype='int')
horizon3 = np.zeros(nx,dtype='int')
horizon31 = np.zeros(nx,dtype='int')  # Falha do Horizonte 3
horizon4 = np.zeros(nx,dtype='int')
horizon41 = np.zeros(nx,dtype='int')  # Falha no Horizonte 4
horizon5 = np.zeros(nx,dtype='int')
horizon51 = np.zeros(nx,dtype='int')


z0, z1, z2, z3, z4, z5, z6, z7 = (nz // 3), (nz // 2.5), (nz // 1.45), (nz // 1), (nz // 1.53), (nz // 1.05), (nz // 1), (nz // 0.92)
height, height1, height2, height3, height4 = 60, 90, 70, 90, 170
L, L1, L2, L3, L4 = (2 * nx), (2 * nx), (1.8 * nx), (1.9 * nx), (8 * nx)

for i in range(nx):
    horizon1[i] = int(z0 + height * np.cos(2*np.pi*(i) / L + np.pi))
    horizon2[i] = int(z1 + height1 * np.cos(2*np.pi*(i) / L1 + np.pi))
    horizon3[i] = int(z2 + height2 * np.sin(2*np.pi*(i) / L2 + np.pi))
    horizon31[i] = int(z4 + height2 * np.sin(2*np.pi*(i) / L2 + np.pi))

    horizon4[i] = int(z3 + height3 * np.sin(2*np.pi*(i) / L3 + np.pi))
    horizon41[i] = int(z5 + height3 * np.sin(2*np.pi*(i) / L3 + np.pi))

    horizon5[i] = int(z6 + height4 * np.sin(2*np.pi*(i) / L4 + np.pi))
    horizon51[i] = int(z7 + height4 * np.sin(2*np.pi*(i) / L4 + np.pi))
"""

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

#velocidade = matriz_complexa(nz, nx, velocidade, horizon2, vel[2])

"""for i in range(nx):
    for j in range(nz):
        if (j >= horizon1[i]):
            velocidade[j,i] = vel[1]
        if (j >= horizon2[i]):
            velocidade[j,i] = vel[2]
            
        if (j >= horizon2[i]):
            velocidade[j,i] = vel[2]
        if (j >= horizon3[i]):
            velocidade[j,i] = vel[3]
        elif (j >= horizon31[i]):
            velocidade[j,90:120] = vel[3]
        if (j >= horizon4[i]):
            velocidade[j,i] = vel[4]
        if (j >= horizon41[i]):
            velocidade[j,90:120] = vel[4]
        if (j >= horizon5[i]):
            velocidade[j,i] = 1600
        if (j >= horizon51[i]):
            velocidade[j,90:120] = 1600"""
#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#

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
