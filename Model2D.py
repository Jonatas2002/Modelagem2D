import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------
#---------------------------------------------------------

## Parametros
nx = 501
nz = 501
dx = 1

VP = np.zeros(nz)
VS = np.zeros(nz)
RHOB = np.zeros(nz)

depth = np.arange(nz) * dx

prof = np.array([100, 120, 300, 400, 501])
vp = np.array([300, 800, 1200, 2200, 3000])
vs = np.array([173, 462, 693, 1270, 1732])
rhob = np.array([957, 1223, 1354, 1575, 1702])

#---------------------------------------------------------
#---------------------------------------------------------

# Preenchendo a matriz vp, vs e rhob com loop
vp_interfaces = []
vs_interfaces = []
rhob_interfaces = []

for i in range (len(prof)):
    start_depth = int(prof[i - 1] / dx) if i > 0 else 0
    end_depth = prof[i] / dx
    vel_p = vp[i]
    vel_s = vs[i]
    densidade = rhob[i]
    vp_interfaces.append((start_depth, end_depth, vel_p))
    vs_interfaces.append((start_depth, end_depth, vel_s))
    rhob_interfaces.append((start_depth, end_depth, densidade))
    
for j in range (len(vp_interfaces)):
    VP_start, VP_end, vel_p = vp_interfaces[j]
    VP_start_depth = int(VP_start)
    VP_end_depth = int(VP_end)
    VP[VP_start_depth: VP_end_depth] = vel_p
    
    VS_start, VS_end, vel_s = vs_interfaces[j]
    VS_start_depth = int(VS_start)
    VS_end_depth = int(VS_end)
    VS[VS_start_depth: VS_end_depth] = vel_s
    
    RHOB_start, RHOB_end, densidade = rhob_interfaces[j]
    RHOB_start_depth = int(RHOB_start)
    RHOB_end_depth = int(RHOB_end)
    RHOB[RHOB_start_depth: RHOB_end_depth] = densidade

#---------------------------------------------------------
#---------------------------------------------------------

# transformando em um array 2D
vp_2D = np.array([VP] * nx).T
vs_2D = np.array([VS] * nx).T
rhob_2D = np.array([RHOB] * nx).T

#---------------------------------------------------------
#---------------------------------------------------------


# Geometria de aquisição

# Fonte
src = np.array([10])

# profundidade da fonte
z_src = np.zeros(len(src))
z_src[:] = prof[0]

src_shot = 1
srcindex = []
while src_shot !=len(src) + 1:
    srcindex.append(src_shot)
    src_shot = src_shot + 1

#---------------------------------------------------------

# Receptor
offset = src[0] + 10
rec = []
while offset !=500:
    rec.append(offset)
    offset = offset + 10

# Profundidade do receptor      
z_rec = np.zeros(len(rec))
z_rec[:] = 100

shot = 1
reciveindex = []
while shot !=len(rec) + 1:
    reciveindex.append(shot)
    shot = shot + 1

#---------------------------------------------------------
#---------------------------------------------------------

# Plot dos modelos
plt.figure(figsize = (24,8))

plt.subplot(131)
plt.title('VP (m/s)')
plt.imshow(vp_2D, aspect='auto', extent= (0, nx*dx, nz*dx, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 4)
plt.plot(rec, z_rec, '*', color='yellow', label='Receptor', markersize= 4)
plt.xlabel('Distâcia (m)')
plt.ylabel('Profundidade (m)')

plt.subplot(132)
plt.title('VS (m/s)')
plt.imshow(vs_2D, aspect='auto', extent= (0, nx*dx, nz*dx, 0),  cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 4)
plt.plot(rec, z_rec, '*', color='yellow', label='Receptor', markersize= 4)
plt.xlabel('Distâcia (m)')
#plt.ylabel('Profundidade (m)')

plt.subplot(133)
plt.title('RHOB (kg/m³)')
plt.imshow(rhob_2D, aspect='auto', extent= (0, nx*dx, nz*dx, 0), cmap='jet')
plt.plot(src, z_src, 'v', color='red', label='Fonte', markersize= 4)
plt.plot(rec, z_rec, '*', color='yellow', label='Receptor', markersize= 4)
plt.xlabel('Distâcia (m)')
#plt.ylabel('Profundidade (m)')

plt.savefig('2DModels.png')
plt.tight_layout()
plt.show()

#---------------------------------------------------------
#---------------------------------------------------------

# Salvando os modelos em binarios
vp_2D.T.astype('float32', order= 'F').tofile(f'vp_2D_{nz}x{nx}_{dx:.0f}m.bin')
vs_2D.T.astype('float32', order= 'F').tofile(f'vs_2D_{nz}x{nx}_{dx:.0f}m.bin')
rhob_2D.T.astype('float32', order= 'F').tofile(f'rhob_2D_{nz}x{nx}_{dx:.0f}m.bin')

# Criando e salvando tabela de fontesd
src_table = np.zeros((len(src), 4))
src_table[:, 0] = srcindex
src_table[:, 1] = srcindex
src_table[:, 2] = src
src_table[:, 3] = z_src
np.savetxt('src_table', src_table, fmt = '%.2f')

# Criando e salvando tabela de receptores
rec_table = np.zeros((len(rec), 4))
rec_table[:, 0] = reciveindex
rec_table[:, 1] = reciveindex
rec_table[:, 2] = rec
rec_table[:, 3] = z_rec
np.savetxt('rec_table', rec_table, fmt = '%.2f')