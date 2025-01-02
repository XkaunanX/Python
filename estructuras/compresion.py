# 05_comprension_listas/comprension_listas.py

# Crear una lista con comprensión
numeros = [x * 2 for x in range(10)]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Filtrar los números pares
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Crear una lista de tuplas con números y sus cuadrados
cuadrados = [(x, x**2) for x in range(5)]  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

print(numeros)
print(pares)
print(cuadrados)
