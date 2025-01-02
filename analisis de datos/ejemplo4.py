import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Crear un gráfico de barras que muestra la tasa de supervivencia por clase
sns.barplot(x='Pclass', y='Survived', data=data)

# Agregar título y etiquetas
plt.title("Tasa de Supervivencia por Clase de Pasajero")
plt.xlabel("Clase de Pasajero")
plt.ylabel("Tasa de Supervivencia")

# Mostrar el gráfico
plt.show()
