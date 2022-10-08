# En este archivo consignaremos las funciones que para la primera parte de construcción de un modelo de regresión se requieren 
# En especial las funciones necesarias para el trabajo en las páginas 67 a 80. 

def obtener_datos(datos_csv):
    from pathlib import Path
    import pandas as pd
    import tarfile
    import urllib.request
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))



if __name__=='__main__':
    obtener_datos(datos_csv)