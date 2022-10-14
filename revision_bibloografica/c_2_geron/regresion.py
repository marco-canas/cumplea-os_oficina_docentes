# En este archivo consignaremos las funciones que para la primera parte de construcción de un modelo de regresión se requieren 
# En especial las funciones necesarias para el trabajo en las páginas 67 a 80. 
# https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb

def obtener_datos(datos_url):
    '''
    INPUT: Le entra la url de ubicación de los datos
    OUTPUT: el dataframe de los datos
    '''
    import pandas as pd
    return pd.read_csv(datos_url) 

def visualizarMatrizHistogramas(dataframe):
    import matplotlib.pyplot as plt
    dataframe.hist(bins=50, figsize=(20,15))
    plt.show()
    return 

if __name__=='__main__':
    pass 
