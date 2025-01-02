# 06_iteradores/iteradores.py

# Crear un iterador con una lista
mi_lista = [1, 2, 3, 4, 5]
iterador = iter(mi_lista)

# Usar next() para obtener elementos
print(next(iterador))  # Imprime 1
print(next(iterador))  # Imprime 2

# Usar un ciclo for con el iterador
for item in iterador:
    print(item)  # Imprime 3, 4, 5
