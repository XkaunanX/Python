from collections import deque

# Crear una cola (deque)
cola = deque([1, 2, 3])

# Añadir elementos al final (enqueue)
cola.append(4)

# Eliminar elementos desde el principio (dequeue)
print(cola.popleft())  # Imprime 1

# Ver la cola
print(cola)  # deque([2, 3, 4])
