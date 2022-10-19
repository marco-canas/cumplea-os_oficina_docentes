# En este archivo consignaremos las funciones que para la primera parte de construcción de un modelo de regresión se requieren 
# En especial las funciones necesarias para el trabajo en las páginas 67 a 80. 
# https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb

def obtener_datos(datos_url):
    '''
    INPUT: Le entra la url de ubicación de los datos
    OUTPUT: el dataframe de los datos
    '''
    import pandas as pd
    import numpy as np 
    return pd.read_csv(datos_url) 

def visualizarMatrizHistogramas(dataframe):
    import pandas as pd 
    return dataframe.hist(bins=50, figsize=(20,15))
    
     

def dividir_entrenamiento_testeo(dataframe):
    '''
    INPUT: 
    datframe en la forma [X|y]
    OUTPUT:
    arreglos de numpy X_train, X_test, y_train, y_test
    '''
    import pandas as pd 
    X = dataframe.drop(['precio'], axis = 1).values
    y = dataframe.precio.values
    from sklearn.model_selection import train_test_split
    X_trian, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, stratify=None, random_state=42 )
    return  X_trian, X_test, y_train, y_test     


def codificar_variables_ordinales():
    from sklearn.preprocessing import OrdinalEncoder
    ordinal_encoder = OrdinalEncoder()
    return ordinal_encoder.fit_transform(atributo_cat)






if __name__=='__main__':
    pass 
