import numpy as np
import matplotlib.pyplot as plt
from time_travel_wave2 import direct_wave
from time_travel_wave2 import refracted_waves
from time_travel_wave2 import reflected_wave


nx = 1160
dtf = 0.8
dt0 = 0.1
offset_max = 576
space = 8

vp = np.array([300, 800, 1200, 2200, 3000])
vs = np.array([173, 462, 693, 1270, 1732])

# Geometria
src = np.array([576])

rec = np.arange(space, (2*offset_max) + space + 1, space)
# onda direta
x1, t1, distance1 = direct_wave(vp[0], rec, src, dtf, dt0, offset_max, space)
x2, t2, distance2 = direct_wave(vp[1], rec, src, dtf, dt0, offset_max, space)
x3, t3, distance3 = direct_wave(vs[1], rec, src, dtf, dt0, offset_max, space)









# Onda refratada
x_refr, t_refr = refracted_waves(vp[1], vp[2], offset_max, space, dtf, dt0, nx)

# Onda refletida
# dt0_refl = 0.4
t0 = 0.472
t_refl1, distance_refl = reflected_wave(vp[1], t0, src, rec)

t0_1 = 0.62
t_refl2, distance_refl2 = reflected_wave(vp[2], t0_1, src, rec)

plt.figure(figsize=(10,10))
# plot onda direta
plt.plot(distance1, abs(t1), 'blue')
plt.plot(distance2, abs(t2), 'red')
plt.plot(distance3, abs(t3), 'green')

# plt.plot(-x1 + 1160, t1, 'blue')
# plt.plot(-x2 + 1160, t2, 'red')
# plt.plot(-x3 + 1160, t3, 'green')

# # plot onda refratada
# plt.plot(x_refr, t_refr, 'black')  # Está sobre t2
# plt.plot(-x_refr + 1160, t_refr, 'black')  # Está sobre t2

# # plot onda relfetida
plt.plot(distance_refl,t_refl1, 'yellow')
plt.plot(distance_refl2,t_refl2, 'orange')

# plt.plot(x_refl2,t_refl2, "orange")

# plt.plot(-x_refl1+1160,t_refl1, 'yellow' )
# plt.plot(-x_refl2 + 1160,t_refl2, 'orange')

plt.grid()
plt.gca().invert_yaxis()
plt.ylim(0.8, 0)

plt.show()

print(distance_refl)