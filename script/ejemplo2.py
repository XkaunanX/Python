import psutil

# Obtener el uso de memoria
memoria = psutil.virtual_memory()

# Mostrar resultados
print(f"Memoria total: {memoria.total / (1024 ** 3):.2f} GB")
print(f"Memoria usada: {memoria.used / (1024 ** 3):.2f} GB")
print(f"Memoria libre: {memoria.available / (1024 ** 3):.2f} GB")
print(f"Porcentaje usado: {memoria.percent}%")
