# En este archivo consignaremos las funciones que para la primera parte de construcción de un modelo de regresión se requieren 
# En especial las funciones necesarias para el trabajo en las páginas 67 a 80. 
# https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb

def obtener_datos(datos_url):
    '''
    # documentación de esta función 
    '''
    import pandas as pd
    return pd.read_csv(datos_url)



if __name__=='__main__':
    pass 
