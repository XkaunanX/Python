# encapsulamiento.py

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Getter para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Setter para modificar el saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad no válida para depósito")

    # Método privado que no puede ser accedido fuera de la clase
    def __ver_titular(self):
        print(f"Titular de la cuenta: {self.__titular}")

# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan", 1000)

# Llamar a los métodos públicos
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # Imprime: 1500

# Intentar acceder a un atributo privado fuera de la clase
# print(cuenta.__titular)  # Error

# Llamar al método privado (esto causará error si se llama fuera de la clase)
# cuenta.__ver_titular()  # Error
