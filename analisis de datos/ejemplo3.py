import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Calcular la matriz de correlación
correlation_matrix = data.corr()

# Visualizar la matriz de correlación con un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Agregar título
plt.title("Matriz de Correlación entre Variables")

# Mostrar el gráfico
plt.show()
