import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Visualizar la distribución de la variable 'Age'
sns.histplot(data['Age'], kde=True, bins=30, color='skyblue')

# Agregar título y etiquetas
plt.title("Distribución de la Edad de los Pasajeros")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

# Mostrar el gráfico
plt.show()
