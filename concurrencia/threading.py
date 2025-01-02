import threading
import time

def tarea(nombre, duracion):
    print(f"Iniciando tarea {nombre}")
    time.sleep(duracion)
    print(f"Tarea {nombre} finalizada")

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("A", 2))
hilo2 = threading.Thread(target=tarea, args=("B", 4))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

print("Todas las tareas han finalizado")