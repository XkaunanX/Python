import asyncio
import time

def tarea_bloqueante(nombre, duracion):
    print(f"Iniciando tarea bloqueante {nombre}")
    time.sleep(duracion)
    print(f"Tarea bloqueante {nombre} finalizada")

async def main():
    loop = asyncio.get_running_loop()
    # Ejecutar función bloqueante en un hilo separado
    await asyncio.gather(
        loop.run_in_executor(None, tarea_bloqueante, "A", 2),
        loop.run_in_executor(None, tarea_bloqueante, "B", 3),
        loop.run_in_executor(None, tarea_bloqueante, "C", 1)
    )

asyncio.run(main())