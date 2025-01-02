import array

# Crear un array de enteros
arr = array.array('i', [1, 2, 3, 4, 5])

# Acceder a un elemento
print(arr[2])  # Imprime 3

# Añadir un nuevo elemento
arr.append(6)

# Ver el array
print(arr)  # array('i', [1, 2, 3, 4, 5, 6])
