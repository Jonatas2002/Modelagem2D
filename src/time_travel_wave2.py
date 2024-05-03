import numpy as np

# Equação para onda direta
def direct_wave(velocity, rec, src, dtf, dt0, offset_max, space):
    
    """ velocity = velocidade de propagação da onda
        dtf = tempo final de chegada da onda
        dt0 = tempo inicial de propagação da onda
        offset_max = maior distancia entre a fonte e receptor
        space = espaçamento entre os receptores """
        
    distance = np.zeros(len(rec))

    for i in range(len(rec)):
        distance[i] = src[0] - rec[i]

    start_distance = offset_max + space
    end_dist = (velocity * (dtf - dt0)) + offset_max
    x = np.linspace(start_distance, end_dist, len(rec))

    t = ((distance - start_distance)/velocity) - dt0
    return x, t, distance

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# Equação para onda refratada
def refracted_waves(velocity1, velocity2, offset_max, space, dtf, dt0, nx):
    start_dist = offset_max + space
    end_dist = (velocity2 * (dtf - dt0)) + offset_max  # Conferir no sismograma qual velocidade usar
    x = np.linspace(start_dist, end_dist, nx)
    deslocamento = offset_max - velocity2 * dt0  # Conferir no sismograma qual velocidade usar

    h = (velocity1 * dt0)/2
    arg = (2*h * (velocity2**2 - velocity1**2)**0.5)/(velocity1*velocity2)
    t = arg + ((x - deslocamento)/velocity2)

    return x, t

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# Equação para onda refletida tipo1
def reflected_wave(velocity,t0, src, rec):
    #start_dist = offset_max + space
    #end_dist = (velocity * (distance - dt0)) + offset_max  # Conferir no sismograma qual velocidade usar
    
    distance = np.zeros(len(rec))

    for i in range(len(rec)):
        distance[i] = src[0] - rec[i]
    
    #x = np.linspace(offset_max, 1160, nx)
    #deslocamento = offset_max - velocity * dt0  # Conferir no sismograma qual velocidade usar

    t = np.sqrt((((distance - 584)**2) / velocity**2) + t0**2)
    return t, distance