# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Paso 1: Recolección de Datos
print("Cargando datos...")
data = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/bank_marketing.csv')

# Mostrar los primeros registros
print("Vista inicial de los datos:")
print(data.head())

# Paso 2: Limpieza y Preparación de Datos
print("\nVerificando valores faltantes...")
print(data.isnull().sum())

print("\nTransformando variables categóricas a numéricas...")
data = pd.get_dummies(data, drop_first=True)

print("\nInformación después de la transformación:")
print(data.info())

# Paso 3: Análisis Exploratorio de Datos (EDA)
print("\nRealizando análisis exploratorio...")

# Distribución de la variable objetivo
sns.countplot(data['y_yes'])
plt.title("Distribución de clientes que hicieron un depósito")
plt.show()

# Correlaciones entre variables
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title("Matriz de Correlación")
plt.show()

# Paso 4: División del Conjunto de Datos
print("\nDividiendo datos en entrenamiento y prueba...")
X = data.drop('y_yes', axis=1)
y = data['y_yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Dimensiones del conjunto de entrenamiento: {X_train.shape}")
print(f"Dimensiones del conjunto de prueba: {X_test.shape}")

# Paso 5: Modelado Predictivo
print("\nEntrenando el modelo de Regresión Logística...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\nHaciendo predicciones...")
y_pred = model.predict(X_test)

# Paso 6: Evaluación del Modelo
print("\nEvaluando el modelo...")
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title("Matriz de Confusión")
plt.xlabel("Predicciones")
plt.ylabel("Valores Reales")
plt.show()

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# Paso 7: Conclusión
print("\nConclusión: Analizar las métricas para mejorar el modelo en futuras iteraciones.")