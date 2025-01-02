# 03_conjuntos/conjuntos.py

# Crear un conjunto
conjunto1 = {1, 2, 3, 4, 5}

# Agregar un elemento
conjunto1.add(6)

# Eliminar un elemento
conjunto1.remove(3)

# Operaciones de conjunto
conjunto2 = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = conjunto1 | conjunto2  # {1, 2, 4, 5, 6, 7, 8}

# Intersección de conjuntos
interseccion = conjunto1 & conjunto2  # {4, 5, 6}

# Diferencia de conjuntos
diferencia = conjunto1 - conjunto2  # {1, 2}

print(union)
print(interseccion)
print(diferencia)
