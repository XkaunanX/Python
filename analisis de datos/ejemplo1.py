import pandas as pd

# Cargar el dataset
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Ver las primeras filas del dataset
print(data.head())

# Descripción estadística de las variables numéricas
print(data.describe())

# Verificar si hay valores faltantes
print(data.isnull().sum())

# Rellenar valores faltantes en la columna 'Age' con la media
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Ver los primeros registros después de la limpieza
print(data.head())
