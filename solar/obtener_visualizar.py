# funciones para leer y visualizar datos

def obtener_datos(datos_feos):
	import numpy as np 
	import pandas as pd 
	datos_bonitos = pd.read_csv(datos_feos)
	return datos_bonitos

if __name__=='__main__':
	obtener_datos('valdivia.csv')