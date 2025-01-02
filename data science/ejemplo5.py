import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Paso 1: Cargar el conjunto de datos de ventas
data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)

# Paso 2: Visualizar los datos
data.plot()
plt.title("Número de pasajeros mensuales")
plt.show()

# Paso 3: Modelo de Holt-Winters (suavizado exponencial)
model = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=12)
model_fit = model.fit()

# Paso 4: Realizar predicciones
forecast = model_fit.forecast(steps=12)
plt.plot(data, label="Datos reales")
plt.plot(forecast, label="Predicción", color='red')
plt.title("Predicción de ventas futuras")
plt.legend()
plt.show()
