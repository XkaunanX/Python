# decoradores.py

# Decorador para medir el tiempo de ejecución de una función
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return wrapper

# Usando el decorador
@medir_tiempo
def ejemplo_lento():
    time.sleep(2)
    print("Ejemplo lento ejecutado")

ejemplo_lento()
