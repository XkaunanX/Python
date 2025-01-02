# funciones.py
# Definición y uso de funciones, incluyendo funciones lambda

# Función simple
def saludar(nombre):
    return f"Hola, {nombre}!"

# Función con valor por defecto
def suma(a, b=5):
    return a + b

# Función lambda para sumar
suma_lambda = lambda a, b: a + b

# Función lambda para comprobar si un número es par
es_par = lambda x: x % 2 == 0

# Llamada a funciones
print(saludar("Juan"))
print(suma(10))  # Usando el valor por defecto de b
print(suma(10, 3))  # Pasando ambos argumentos

# Llamada a la función lambda
print("Suma (10, 3) usando lambda:", suma_lambda(10, 3))

# Comprobación de si un número es par
numero = 4
print(f"¿El número {numero} es par?", es_par(numero))

numero = 7
print(f"¿El número {numero} es par?", es_par(numero))
