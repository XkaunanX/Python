from concurrent.futures import ThreadPoolExecutor
import time

def tarea(nombre, duracion):
    print(f"Iniciando tarea {nombre}")
    time.sleep(duracion)
    print(f"Tarea {nombre} finalizada")

with ThreadPoolExecutor(max_workers=3) as executor:
    # Ejecutar varias tareas
    executor.submit(tarea, "A", 2)
    executor.submit(tarea, "B", 3)
    executor.submit(tarea, "C", 1)
    executor.submit(tarea, "D", 4)