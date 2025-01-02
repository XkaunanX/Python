# herencia.py

# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Subclases deben implementar este método")

# Clase hija que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de las clases hijas
perro = Perro("Rex")
gato = Gato("Whiskers")

# Llamar a los métodos de las subclases
print(perro.hacer_sonido())  # Imprime: Guau
print(gato.hacer_sonido())   # Imprime: Miau
