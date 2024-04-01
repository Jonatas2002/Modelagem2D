import numpy as np

# Equação para onda direta
def direct_wave(velocity, dtf, dt0, offset_max, space, nx):
    
    """ velocity = velocidade de propagação da onda
        dtf = tempo final de chegada da onda
        dt0 = tempo inicial de propagação da onda
        offset_max = maior distancia entre a fonte e receptor
        space = espaçamento entre os receptores """

    start_dist = offset_max + space
    end_dist = (velocity * (dtf - dt0)) + offset_max
    x = np.linspace(start_dist, end_dist, nx)
    deslocamento = offset_max - velocity * dt0
    t = (x - deslocamento)/velocity
    return x, t

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
def reflected_wave(velocity2, offset_max, space, distance, dt0, nx ):
    start_dist = offset_max + space
    end_dist = (velocity2 * (distance - dt0)) + offset_max  # Conferir no sismograma qual velocidade usar
    x = np.linspace(offset_max, 1160, nx)
    deslocamento = offset_max - velocity2 * dt0  # Conferir no sismograma qual velocidade usar

    h = (velocity2 * dt0)/2
    t = np.sqrt((x-deslocamento)**2 + 4*h**2)/velocity2

    return x, t