# Importar as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from function import horizon_sin
from function import matriz_complexa


"""## Modelo de velocidade 2D """
x = 4000
z = 400
dx = 1
nx = int(x/dx + 1)
nz = int(z/dx + 1)

depth = np.arange(nz) * dx

# Velocidade e Densidade das camadas
vp = np.array([300, 800, 1200, 2200, 3000])
vs = np.array([173, 462, 693, 1270, 1732])
rhob = np.array([957, 1223, 1354, 1575, 1702])
# Construção da Matriz de Velocidade

#horizon1 = horizon_reta(nx, a=5, b=1)
horizon1 = horizon_sin(nz, nx, z0=4.52, height=37.5, L=2.0)
horizon2 = horizon_sin(nz, nx, z0=2.90, height=37.5, L=2.0)
horizon3 = horizon_sin(nz, nx, z0=1.68, height=37.5, L=2.0)
horizon4 = horizon_sin(nz, nx, z0=1.18, height=37.5, L=2.0)


VP = np.zeros((nz, nx)) + vp[0]
VP = matriz_complexa(nz, nx, VP, horizon1, vp[1])
VP = matriz_complexa(nz, nx, VP, horizon2, vp[2])
VP = matriz_complexa(nz, nx, VP, horizon3, vp[3])
#VP = matriz_complexa(nz, nx, VP, horizon4, vp[4])

VS = np.zeros((nz, nx)) + vs[0]
VS = matriz_complexa(nz, nx, VS, horizon1, vs[1])
VS = matriz_complexa(nz, nx, VS, horizon2, vs[2])
VS = matriz_complexa(nz, nx, VS, horizon3, vs[3])
#VS = matriz_complexa(nz, nx, VS, horizon4, vs[4])

RHOB = np.zeros((nz, nx)) + rhob[0]
RHOB = matriz_complexa(nz, nx, RHOB, horizon1, rhob[1])
RHOB = matriz_complexa(nz, nx, RHOB, horizon2, rhob[2])
RHOB = matriz_complexa(nz, nx, RHOB, horizon3, rhob[3])
#RHOB = matriz_complexa(nz, nx, RHOB, horizon4, rhob[4])


#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#
# Geometria de aquisição

offset_min = 0
offset_max = 576
space = 8

# Fonte
src = np.arange(offset_max + space, (x - offset_max + space), space)

# profundidade da fonte
z_src = []
for i in range(offset_max + space, (x - offset_max + space), space):
    z_src.append(horizon1[i])
srcindex = np.arange(1, len(src) + 1, space)

#---------------------------------------------------------

# Receptor
rec1 = np.arange(space, x + 1, space)

# Profundidade do receptor      
z_rec = []

for i in range(7, len(horizon1), 8):
    z_rec.append(horizon1[i])

reciveindex = np.arange(1, len(rec1) + 1, 1)
#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#

# Plot dos graficos
plt.figure(figsize=(10,8))

plt.subplot(311)
plt.imshow(VP, aspect='auto',extent=(0, nx*dx, nz*dx, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.title('Velocidade P')
plt.xlabel('Distância (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='VP (m/s)')

plt.subplot(312)
plt.imshow(VS, aspect='auto',extent=(0, nx*dx, nz*dx, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.title('Velocidade S')
plt.xlabel('Distância (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='VS (m/s)')

plt.subplot(313)
plt.imshow(RHOB, aspect='auto',extent=(0, nx*dx, nz*dx, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.title('Densidade')
plt.xlabel('Distância (m)')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='RHOB (kg/m³)')

plt.tight_layout()
plt.show()

#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#
teste = VP[86,:]
print(z_rec)