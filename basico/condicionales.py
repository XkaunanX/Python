# condicionales.py
# Condicionales if, elif, else, switch (simulado) y match

# Condicionales if, elif, else
edad = 20

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor de 65 años")

# Simulación de un switch con un diccionario
def switch_example(opcion):
    # Usamos un diccionario para simular el switch
    switch = {
        1: "Opción 1 seleccionada",
        2: "Opción 2 seleccionada",
        3: "Opción 3 seleccionada",
    }
    return switch.get(opcion, "Opción no válida")  # Si no se encuentra la opción, devuelve "Opción no válida"

# Ejemplo de uso del switch simulado
opcion_seleccionada = 2
print(switch_example(opcion_seleccionada))  # Debería imprimir "Opción 2 seleccionada"

# Uso del match (disponible a partir de Python 3.10)
opcion_match = 3

match opcion_match:
    case 1:
        print("Opción 1 seleccionada usando match")
    case 2:
        print("Opción 2 seleccionada usando match")
    case 3:
        print("Opción 3 seleccionada usando match")
    case _:
        print("Opción no válida usando match")  # El caso "_" es un comodín que captura cualquier otro valor

# Más ejemplos de uso de condicionales
numero = 10
if numero > 5 and numero < 15:
    print(f"{numero} está entre 5 y 15")
elif numero >= 15:
    print(f"{numero} es mayor o igual a 15")
else:
    print(f"{numero} es menor o igual a 5")
