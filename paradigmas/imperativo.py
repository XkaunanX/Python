# Función para calcular el factorial de un número
def calcular_factorial(n):
    resultado = 1  # Inicializamos el resultado como 1

    # Utilizamos un bucle para calcular el factorial
    for i in range(1, n + 1):  # Bucle de 1 a n
        resultado *= i  # Multiplicamos el resultado por el número en cada iteración
    
    return resultado  # Retornamos el resultado final

# Solicitar al usuario un número
numero = int(input("Ingresa un número para calcular su factorial: "))

# Calcular el factorial
factorial = calcular_factorial(numero)

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}")