# 01_listas/listas.py

# Crear una lista
frutas = ['manzana', 'banana', 'cereza']

# Agregar un elemento al final
frutas.append('naranja')

# Insertar un elemento en una posición específica
frutas.insert(1, 'kiwi')

# Eliminar un elemento por valor
frutas.remove('banana')

# Eliminar un elemento por índice
del frutas[2]

# Listas anidadas
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acceder a un elemento de la lista anidada
print(listas_anidadas[1][2])  # Imprime 6

# Imprimir lista final
print(frutas)
