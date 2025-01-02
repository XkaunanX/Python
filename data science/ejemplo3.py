import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Paso 1: Cargar el conjunto de datos
data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Housing.csv')

# Paso 2: Preparación de los datos
X = data.drop('MEDV', axis=1)  # Variables predictoras
y = data['MEDV']  # Variable objetivo (precio de la vivienda)

# Paso 3: División del conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Paso 5: Predicción y evaluación
y_pred = model.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"R^2: {r2}")

# Visualización de resultados
plt.scatter(y_test, y_pred)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Predicción de precios de viviendas")
plt.show()
