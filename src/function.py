import numpy as np

# Modelo 1D
def model_1D(nz, dx, dimensao, valor):
    """ Função responsavel pela criação de matrizes 1D utilizada para contrução de modelos
        de velocidade, densidade e outras utilidades"""
    M = np.zeros(nz)
    
    for i in range(len(dimensao)):
        start_dimensao = int(dimensao[i - 1] / dx) if i > 0 else 0
        end_dimensao = int(dimensao[i] // dx)
        M[start_dimensao:end_dimensao] = valor[i]

    return M

# Modelo 1D
def model_paralelo_2D(nz, nx, dx, dimensao, modelo):
    """Função responsavel pela criação de matrizes 2D utilizada para contrução de modelos sismico
        plano paralelo além de outras utilidades."""
    
    M = np.zeros((nz, nx))
    
    for i in range(len(dimensao)):
        start_dimensao = int(dimensao[i - 1] / dx) if i > 0 else 0
        end_dimensao = int(dimensao[i] // dx)
        M[start_dimensao:end_dimensao, :] = modelo[i]
    
    return M

# ------------------------------------------------------------
#---------------------------------------------------------------

# Construção da Matriz de Velocidade e

def horizon_cos(nz, nx, z0, height, L):
    '''Exemplo de uso:
        
        Z0(float): Posição inicial do horizonte na direção vertical
                    - Quanto maior o valor de z0, mais raso estará o horizonte
                    - Quanto menor o valor de z0, mais fundo estará o horizonte
                    
        height(float): Amplitude do Horizonte
                    - Quanto maior o valor de height, maior sua amplitude
        
        L(float): Comprimento da função
                    - Quanto maior o valor de L, menor será o comprimento
                    - 1 representa o comprimento total de 1 periodo da função'''
                    
    #velocidade = np.zeros((nz, nx)) + model[0]
    horizon = np.zeros(nx,dtype='int')
    
    Z0 = (nz // z0)
    HEIGHT = height
    LL = (L * nx)
    
    for i in range(nx):
        horizon[i] = int(Z0 + HEIGHT * np.cos(2*np.pi*(i) / LL + np.pi))
        
    return horizon

def horizon_sin(nz, nx, z0, height, L):
    '''Exemplo de uso:
        
        Z0(float): Posição inicial do horizonte na direção vertical
                    - Quanto maior o valor de z0, mais raso estará o horizonte
                    - Quanto menor o valor de z0, mais fundo estará o horizonte
                    
        height(float): Amplitude do Horizonte
                    - Quanto maior o valor de height, maior sua amplitude
        
        L(float): Comprimento da função
                    - Quanto maior o valor de L, menor será o comprimento
                    - 1 representa o comprimento total de 1 periodo da função'''
                    
    #velocidade = np.zeros((nz, nx)) + model[0]
    horizon = np.zeros(nx,dtype='int')
    
    Z0 = (nz // z0)
    HEIGHT = height
    LL = (L * nx)
    
    for i in range(nx):
        horizon[i] = int(Z0 + HEIGHT * np.sin(2*np.pi*(i) / LL + np.pi))
        
    return horizon

# ------------------------------------------------------------
#---------------------------------------------------------------

def horizon_reta(nx, a, b):
    ''' Exemplo de uso:
        y = a + bx
        b: coeficiente angular da reta
        c = coeficiente linear da reta'''
    horizon = np.zeros(nx,dtype='int')
    
    m = b # Inclinação
    
    for i in range(nx):
        horizon[i] = int(m * i + a) 
    
    return horizon 
 



def matriz_complexa(nz, nx, velocidade, horizonte, valor):
    for i in range(nx):
        for j in range(nz):
            if (j >= horizonte[i]):
                velocidade[j,i] = valor
    return velocidade


def matriz_falha(nz, nx, velocidade, horizonte, valor, If, Ff):
    ''' If = Indice inicial da matriz que começa a falha
        Ff = Indice final da matriz que termina a falha'''
    for i in range(nx):
        for j in range(nz):
            if (j >= horizonte[i]):
                velocidade[j,If:Ff] = valor
    return velocidade

            
       
