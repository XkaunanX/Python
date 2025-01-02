from collections import namedtuple

# Crear una tupla nombrada
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear una instancia de la tupla nombrada
persona1 = Persona(nombre="Juan", edad=30, ciudad="Madrid")

# Acceder a los valores por nombre
print(persona1.nombre)  # Imprime Juan
print(persona1.edad)    # Imprime 30
