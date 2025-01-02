import asyncio

async def tarea(nombre, duracion):
    print(f"Iniciando tarea {nombre}")
    await asyncio.sleep(duracion)
    print(f"Tarea {nombre} finalizada")

async def main():
    # Ejecutar tareas concurrentemente
    await asyncio.gather(
        tarea("A", 2),
        tarea("B", 3),
        tarea("C", 1)
    )

# Ejecutar el loop de eventos
asyncio.run(main())