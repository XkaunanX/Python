from multiprocessing import Pool, cpu_count
import math
import time

# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Función que procesa un rango de números
def primos_en_rango(rango):
    inicio, fin = rango
    return [n for n in range(inicio, fin) if es_primo(n)]

if __name__ == "__main__":
    # Definir el rango de búsqueda
    inicio = 1
    fin = 10_0000
    num_procesos = cpu_count()  # Número de procesadores disponibles

    print(f"Usando {num_procesos} procesos para calcular números primos")

    # Dividir el rango en partes iguales para cada proceso
    rangos = []
    tamanio_bloque = (fin - inicio) // num_procesos
    for i in range(num_procesos):
        inicio_bloque = inicio + i * tamanio_bloque
        fin_bloque = inicio + (i + 1) * tamanio_bloque if i < num_procesos - 1 else fin
        rangos.append((inicio_bloque, fin_bloque))

    # Medir tiempo de ejecución
    inicio_tiempo = time.time()

    # Crear un pool de procesos
    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(primos_en_rango, rangos)

    # Combinar los resultados de todos los procesos
    todos_primos = [primo for sublista in resultados for primo in sublista]

    fin_tiempo = time.time()

    print(f"Se encontraron {len(todos_primos)} números primos")
    print(f"Tiempo total: {fin_tiempo - inicio_tiempo:.2f} segundos")