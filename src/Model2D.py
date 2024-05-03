import numpy as np
import matplotlib.pyplot as plt
from function import model_paralelo_2D

#---------------------------------------------------------
#---------------------------------------------------------

## Parametros
x = 4000
z = 400
dx = 1
dz = 1
nx = int(x/dx +1)
nz = int(z/dz +1)

VP = np.zeros(nz)
VS = np.zeros(nz)
RHOB = np.zeros(nz)

depth = np.arange(nz) * dz

#prof = np.array([100, 120, 300, 400, nz*dx])
#vp = np.array([300, 800, 1200, 2200, 3000])
#vs = np.array([173, 462, 693, 1270, 1732])
#rhob = np.array([957, 1223, 1354, 1575, 1702])

prof = np.array([50, nz*dz])
vp = np.array([300, 800])
vs = np.array([173, 462])
rhob = np.array([957, 1223])

#---------------------------------------------------------
#---------------------------------------------------------

# Construindo modelos
VP = model_paralelo_2D(nz, nx, dz, prof, vp)
VS = model_paralelo_2D(nz, nx, dz, prof, vs)
RHOB = model_paralelo_2D(nz, nx, dz, prof, rhob)

#---------------------------------------------------------
#---------------------------------------------------------

# Geometria de aquisição
offset_min = 0
offset_max = 576
space = 8
# Fonte
#src = np.array([offset_max + space/2])
src = np.arange(576, 3424, 8)
# profundidade da fonte
z_src = np.zeros(len(src))
z_src[:] = prof[0]

srcindex = np.arange(1, len(src) + 1, space)

#---------------------------------------------------------

# Receptor
#offset_min = src[0] + 10
#offset_max = src[0] + 480
#rec = np.arange(offset_min, offset_max + 1, 10)

#rec1 = np.arange(0, (offset_max*2) + 1, space)
rec1 = np.arange(0, 4000 + 1, space)

#print(len(rec1))


# Profundidade do receptor      
z_rec = np.zeros(len(rec1))
z_rec[:] = prof[0]

reciveindex = np.arange(1, len(rec1) + 1, 1)

tabela_relacao = np.zeros((1,3))
tabela_relacao[:,0] = 1
tabela_relacao[:,1] = 1
tabela_relacao[:,2] = (offset_max*2/8)+1

#---------------------------------------------------------
#---------------------------------------------------------

# Plot dos modelos - Vizualização geral dos 3 modelos
plt.figure(figsize=(10,10))

plt.subplot(311)
plt.title('VP (m/s)')
plt.imshow(VP, aspect='auto', extent= (0, nx*dx, nz*dz, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.xlabel('Distâcia (m)')
plt.ylabel('Profundidade (m)')
plt.legend(fontsize='small')
plt.colorbar(label='VP (m/s)')


plt.subplot(312)
plt.title('VS (m/s)')
plt.imshow(VS, aspect='auto', extent= (0, nx*dx, nz*dz, 0),  cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.xlabel('Distâcia (m)')
#plt.yticks([])
plt.legend(fontsize='small')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='VS (m/s)')


plt.subplot(313)
plt.title('RHOB (kg/m³)')
plt.imshow(RHOB, aspect='auto', extent= (0, nx*dx, nz*dz, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 6)
plt.plot(rec1, z_rec, '*', color='yellow', label='Receptor', markersize= 2)
plt.xlabel('Distâcia (m)')
#plt.yticks([])
plt.legend(fontsize='small')
plt.ylabel('Profundidade (m)')
plt.colorbar(label='RHOB (Kg/m³)')


plt.savefig('2DModels.png')
plt.tight_layout()
plt.show()

#---------------------------------------------------------
#---------------------------------------------------------

# Salvando os modelos em binarios
VP.T.astype('float32', order= 'F').tofile(f'vp_2D_{nz}x{nx}_{dx:.0f}m.bin')
VS.T.astype('float32', order= 'F').tofile(f'vs_2D_{nz}x{nx}_{dx:.0f}m.bin')
RHOB.T.astype('float32', order= 'F').tofile(f'rhob_2D_{nz}x{nx}_{dx:.0f}m.bin')

# Criando e salvando tabela de fontesd
#formats = ['%d', '%d', '%.2f', '%.2f']

# src_table = np.zeros((len(src), 4))
# src_table[:, 0] = srcindex
# src_table[:, 1] = srcindex
# src_table[:, 2] = src
# src_table[:, 3] = z_src
# np.savetxt('Tabela de fonte', src_table, delimiter=',', fmt='%.2f')

# # Criando e salvando tabela de receptores
# rec_table = np.zeros((len(rec1), 5))
# rec_table[:, 0] = reciveindex
# rec_table[:, 1] = reciveindex
# rec_table[:, 2] = rec1
# rec_table[:, 3] = z_rec
# np.savetxt('Tabela de Receptores', rec_table, delimiter=',', fmt='%.2f')

# # Criando e salvando tabela de relação
# np.savetxt('tabela_relacao', tabela_relacao, delimiter=',', fmt='%d')

# #---------------------------------------------------------
# #---------------------------------------------------------

teste = VP[50,:]
print(teste)