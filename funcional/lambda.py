# funciones_lambdas.py

# Definición de una función lambda que suma dos números
suma = lambda a, b: a + b
print(f"Resultado de la suma: {suma(3, 4)}")

# Uso de lambda con la función map para multiplicar por 2 cada número en una lista
numeros = [1, 2, 3, 4, 5]
doblados = list(map(lambda x: x * 2, numeros))
print(f"Números doblados: {doblados}")

# Uso de lambda con la función filter para filtrar números mayores que 3
filtrados = list(filter(lambda x: x > 3, numeros))
print(f"Números mayores que 3: {filtrados}")
