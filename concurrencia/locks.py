import threading
import time

lock = threading.Lock()

def tarea_critica(nombre):
    print(f"Tarea {nombre} esperando el lock")
    with lock:
        print(f"Tarea {nombre} accediendo a la sección crítica")
        time.sleep(2)
        print(f"Tarea {nombre} saliendo de la sección crítica")

hilo1 = threading.Thread(target=tarea_critica, args=("A",))
hilo2 = threading.Thread(target=tarea_critica, args=("B",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()