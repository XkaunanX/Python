# map_filter_reduce.py

from functools import reduce

# Ejemplo con map (multiplicar por 2 cada elemento)
numeros = [1, 2, 3, 4, 5]
map_resultado = list(map(lambda x: x * 2, numeros))
print(f"Resultado de map: {map_resultado}")

# Ejemplo con filter (filtrar los números mayores que 3)
filter_resultado = list(filter(lambda x: x > 3, numeros))
print(f"Resultado de filter: {filter_resultado}")

# Ejemplo con reduce (sumar todos los números en la lista)
reduce_resultado = reduce(lambda x, y: x + y, numeros)
print(f"Resultado de reduce: {reduce_resultado}")
