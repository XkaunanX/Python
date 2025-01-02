# Instalación de la librería ordered-set si no la tienes
# pip install ordered-set
from ordered_set import OrderedSet

# Crear un conjunto ordenado
conjunto_ordenado = OrderedSet([1, 2, 3, 4])

# Añadir un elemento
conjunto_ordenado.add(5)

# Ver el conjunto
print(conjunto_ordenado)  # OrderedSet([1, 2, 3, 4, 5])
