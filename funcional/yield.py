# generadores.py

# Definición de un generador que genera los primeros n números
def generar_numeros(n):
    i = 0
    while i < n:
        yield i  # Pausa la función y devuelve el valor de i
        i += 1

# Usamos el generador
gen = generar_numeros(5)
for numero in gen:
    print(f"Número generado: {numero}")

# También podemos convertir el generador en una lista
gen_lista = list(generar_numeros(5))
print(f"Lista de números generados: {gen_lista}")
