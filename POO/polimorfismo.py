# polimorfismo.py

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Función que utiliza polimorfismo
def mostrar_sonido(animal: Animal):
    print(animal.hacer_sonido())

# Crear instancias de las clases
perro = Perro()
gato = Gato()

# Usar polimorfismo para llamar al mismo método en diferentes tipos de objetos
mostrar_sonido(perro)  # Imprime: Guau
mostrar_sonido(gato)   # Imprime: Miau
