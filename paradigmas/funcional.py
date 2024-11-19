# Función pura (transparencia referencial)
def suma(a, b):
    return a + b

# Función de alto orden
def aplicar_operacion(func, x, y):
    """Toma una función y dos argumentos, y aplica la función a esos argumentos."""
    return func(x, y)

# Función que genera una función con un valor fijo
def multiplicar_por(factor):
    """Devuelve una función que multiplica su argumento por un 'factor'."""
    return lambda x: x * factor

def main():
    # Usando la función de alto orden 'aplicar_operacion'
    resultado_suma = aplicar_operacion(suma, 5, 3)
    print(f"Resultado de la suma: {resultado_suma}")  # Debería mostrar: 8

    # Usando la función generadora 'multiplicar_por'
    multiplicar_por_2 = multiplicar_por(2)
    resultado_multiplicacion = multiplicar_por_2(4)
    print(f"Resultado de multiplicar 4 por 2: {resultado_multiplicacion}")  # Debería mostrar: 8

    # Aquí demostramos transparencia referencial:
    # La expresión 'suma(5, 3)' puede ser reemplazada por su valor 8, sin cambiar el comportamiento del programa.
    resultado_suma = 8
    print(f"Resultado después de la sustitución directa: {resultado_suma}")

if __name__ == "__main__":
    main()