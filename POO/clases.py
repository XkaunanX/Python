# clases_objetos.py

# Definición de una clase simple
class Coche:
    # Constructor de la clase
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    # Método de la clase
    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo} de color {self.color}")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Llamar a un método del objeto
mi_coche.mostrar_info()  # Imprime: Coche: Toyota Corolla de color Rojo
