# ciclos.py
# Ciclos for y while

# Ciclo for
print("Ciclo for:")
for i in range(5):  # Imprime de 0 a 4
    print(i)

# Ejemplo de ciclo for que actúa como foreach en Python
frutas = ['manzana', 'banana', 'cereza', 'naranja']

# Iterar sobre cada elemento de la lista
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Ciclo while
print("\nCiclo while:")
contador = 0
while contador < 5:  # Imprime de 0 a 4
    print(contador)
    contador += 1

# Imprimir los números del 1 al 10, pero de dos en dos
for i in range(1, 11, 2):
    print(i)  # Imprime 1, 3, 5, 7, 9
    
frutas = ['manzana', 'banana', 'cereza', 'naranja']

# Obtener índice y valor durante la iteración
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
    
persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Iterar sobre las claves y valores del diccionario
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

nombres = ['Juan', 'Ana', 'Carlos']
edades = [25, 30, 22]

# Iterar sobre ambas listas al mismo tiempo
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# Salir del ciclo cuando encontramos el número 5
for i in range(1, 11):
    if i == 5:
        print("Número 5 encontrado, saliendo del ciclo.")
        break
    print(i)

# Saltar los números impares
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"{i} es par.")

# Crear una lista con los números pares del 1 al 10
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]
