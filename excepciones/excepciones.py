# try_except.py

try:
    # Intentamos dividir entre 0, lo cual generará una excepción
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Capturamos la excepción y mostramos un mensaje
    print(f"Error: {e}")
else:
    # Si no hay error, esta parte del código se ejecutará
    print("Operación exitosa, el resultado es:", resultado)
finally:
    # Este bloque se ejecuta siempre, haya o no haya error
    print("Fin del bloque try-except")
