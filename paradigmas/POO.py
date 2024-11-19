class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Método para saludar a la persona."""
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        """Método para incrementar la edad de la persona en 1."""
        self.edad += 1
        print(f"Ahora tengo {self.edad} años.")

    def cambiar_nombre(self, nuevo_nombre):
        """Método para cambiar el nombre de la persona."""
        self.nombre = nuevo_nombre
        print(f"Ahora me llamo {self.nombre}.")

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nombre, edad)
        self.puesto = puesto

    def mostrar_informacion(self):
        """Método para mostrar la información completa del empleado."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Puesto: {self.puesto}")

    def cambiar_puesto(self, nuevo_puesto):
        """Método para cambiar el puesto del empleado."""
        self.puesto = nuevo_puesto
        print(f"Ahora soy {self.puesto}.")

def mostrar_menu():
    """Función para mostrar el menú al usuario."""
    print("\n--- Menú ---")
    print("1. Ver información del empleado")
    print("2. Saludar")
    print("3. Cumplir un año")
    print("4. Cambiar nombre")
    print("5. Cambiar puesto")
    print("6. Salir")

def main():
    # Crear un objeto Empleado con nombre, edad y puesto iniciales.
    empleado = Empleado("Carlos", 28, "Desarrollador")

    while True:
        mostrar_menu()
        
        # Pedir al usuario que elija una opción
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            empleado.mostrar_informacion()
        elif opcion == '2':
            empleado.saludar()
        elif opcion == '3':
            empleado.cumplir_anios()
        elif opcion == '4':
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            empleado.cambiar_nombre(nuevo_nombre)
        elif opcion == '5':
            nuevo_puesto = input("Introduce el nuevo puesto: ")
            empleado.cambiar_puesto(nuevo_puesto)
        elif opcion == '6':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 6.")

if __name__ == "__main__":
    main()