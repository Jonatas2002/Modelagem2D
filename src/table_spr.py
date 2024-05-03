import numpy as np
import matplotlib.pyplot as plt

# Dados da Geometria
x = 4000
y =1
elev = 10  
space = 8
rec= 500

# Formato das tabelas
format1 = ['%03d', '%06.2f', '%.2f', '%.2f']
format2 = ['%03d', '%03d', '%03d', '%03d', '%03d']
format3 = ['%03d', '%03d', '%.2f', '%.2f', '%.2f', '%.2f']
format4 = ['%03d', '%.2f', '%.2f']

# Criação da Tabela
table_station = np.zeros((rec, 4))
table_station[:, 0] = np.arange(1, rec + 1, 1)  # Station
table_station[:, 1] = np.arange(0, x, 8)        # Coordenada em X
table_station[:, 2] = y                         # Coordenada em T
table_station[:, 3] = elev                      # Elevação

np.savetxt('table_geometry_station.txt', table_station, delimiter= '        ', fmt = format1)
#--------------------------------------------------------------------------------------------#

# Dados da Geometria
offset_max = 576 #(72*8)
shot = 356
rchan_i = 1
rchan_f = 500
r_station_i = 1
r_station_f = 500

# Criação da Tabela
table_relation = np.zeros((shot, 5))
table_relation[:, 0] = np.arange(1, shot + 1, 1)           # Station
table_relation[:, 1] = rchan_i                             # Coordenada em X
table_relation[:, 2] = r_station_i                         # Coordenada em T
table_relation[:, 3] = rchan_f                             # Elevação
table_relation[:, 4] = r_station_f

np.savetxt('table_geometry_relation.txt', table_relation, delimiter= '        ', fmt = format2)
#----------------------------------------------------------------------------------------------#
# Dados da Geometria
shot = 356
station_i = 72
station_f = 427
shot_i_x = 568
shot_f_x = 3408
depth = 10
shot_i_y = 1
shot_f_y = 1

# Criação da Tabela
table_shot = np.zeros((shot, 6))
table_shot[:, 0] = np.arange(1, shot + 1, 1)                # Station
table_shot[:, 1] = np.arange(station_i, station_f + 1, 1)   # Coordenada em X
table_shot[:, 2] = depth                              # Coordenada em T
table_shot[:, 3] = elev                                  # Elevação
table_shot[:, 4] = np.arange(shot_i_x, shot_f_x + 1, 8)
table_shot[:, 5] = shot_i_y


np.savetxt('table_geometry_shot.txt', table_shot, delimiter= '        ', fmt = format3)
#----------------------------------------------------------------------------------------------#
# Dados da Geometria
cdpl = 855
cdp_i = 73
cdp_f = 927
cdp_x_i = 284
cdp_x_f = 3700
cdp_y_i = 1
cdp_y_f = 1

# Criação da Tabela
table_cdp = np.zeros((cdpl, 3))
table_cdp[:, 0] = np.arange(cdp_i, cdp_f + 1, 1)                # Station
table_cdp[:, 1] = np.arange(cdp_x_i, cdp_x_f + 1, 4)   # Coordenada em X
table_cdp[:, 2] = cdp_y_i                              # Coordenada em T


np.savetxt('table_geometry_cdp.txt', table_cdp, delimiter= '        ', fmt = format4)
