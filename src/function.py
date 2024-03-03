import numpy as np

# Modelo 1D
def model_1D(nz, dx, dimensao, valor):
    """ Função responsavel pela criação de matrizes 1D utilizada para contrução de modelos em
        profundidade de velocidade, densidade e outros afins.
        
        A função ainda está passando por alguns testes e será testado em breve em modelos no tempo"""
    M = np.zeros(nz)
    
    for i in range(len(dimensao)):
        start_dimensao = int(dimensao[i - 1] / dx) if i > 0 else 0
        end_dimensao = dimensao[i] // dx
        M[start_dimensao:end_dimensao] = valor[i]

    return M

# Modelo 1D
def model_paralelo_2D(nz, nx, dx, dimensao, modelo):
    """Função responsavel pela criação de matrizes 2D utilizada para contrução de modelos sismico
        plano paralelo em profundidade além de outras utilidades.
        
        A função ainda está passando por alguns testes e será testado em breve em modelos no tempo"""
    
    M = np.zeros((nz, nx))
    
    for i in range(len(dimensao)):
        start_dimensao = int(dimensao[i - 1] / dx) if i > 0 else 0
        end_dimensao = dimensao[i] // dx
        M[start_dimensao:end_dimensao, :] = modelo[i]
    
    return M
