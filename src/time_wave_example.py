import numpy as np
import matplotlib.pyplot as plt
from time_travel_wave import direct_wave
from time_travel_wave import refracted_waves
from time_travel_wave import reflected_wave


nx = 1160
dtf = 0.8
dt0 = 0.1
offset_max = 576
space = 8

vp = np.array([300, 800, 1200, 2200, 3000])
vs = np.array([173, 462, 693, 1270, 1732])

# onda direta
x1, t1 = direct_wave(vp[0], dtf, dt0, offset_max, space, nx)
x2, t2 = direct_wave(vp[1], dtf, dt0, offset_max, space, nx)
x3, t3 = direct_wave(vs[1], dtf, dt0, offset_max, space, nx)

# Onda refratada
x_refr, t_refr = refracted_waves(vp[1], vp[2], offset_max, space, dtf, dt0, nx)

# Onda refletida
dt0_refl = 0.4
x_refl1, t_refl1 = reflected_wave(vp[2], offset_max, space, dtf, dt0_refl, nx )
x_refl2, t_refl2 = reflected_wave(vp[3], offset_max, space, dtf, dt0_refl, nx )

plt.figure(figsize=(10,10))
# plot onda direta
plt.plot(x1, t1, 'blue')
plt.plot(x2, t2, 'red')
plt.plot(x3, t3, 'green')

plt.plot(-x1 + 1160, t1, 'blue')
plt.plot(-x2 + 1160, t2, 'red')
plt.plot(-x3 + 1160, t3, 'green')

# # plot onda refratada
# plt.plot(x_refr, t_refr, 'black')  # Está sobre t2
# plt.plot(-x_refr + 1160, t_refr, 'black')  # Está sobre t2

# plot onda relfetida
plt.plot(x_refl1,t_refl1, 'yellow')
plt.plot(x_refl2,t_refl2, "orange")

plt.plot(-x_refl1+1160,t_refl1, 'yellow' )
plt.plot(-x_refl2 + 1160,t_refl2, 'orange')

plt.grid()
plt.ylim(0.8, 0)

plt.show()
