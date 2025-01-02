# excepciones.py

# Definimos una excepción personalizada
class MiExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

# Función que lanza una excepción personalizada
def verificar_valor(valor):
    if valor < 0:
        raise MiExcepcion("El valor no puede ser negativo")
    else:
        print("El valor es válido:", valor)

# Prueba de la excepción personalizada
try:
    verificar_valor(-10)
except MiExcepcion as e:
    print(f"Se ha producido una excepción: {e}")
