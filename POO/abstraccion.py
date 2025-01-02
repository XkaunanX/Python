# abstraccion.py
from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

# Clase que hereda de Vehiculo
class Coche(Vehiculo):
    def arrancar(self):
        print("Coche arrancado")

    def detener(self):
        print("Coche detenido")

# Crear un objeto de la clase Coche
mi_coche = Coche()
mi_coche.arrancar()  # Imprime: Coche arrancado
mi_coche.detener()   # Imprime: Coche detenido
