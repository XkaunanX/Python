# entradas_salidas.py
# Entrada y salida de datos, manejo de archivos

# Entrada desde teclado
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")

print(f"Tu nombre es {nombre} y tienes {edad} años.")

# Escritura en un archivo
with open("saludo.txt", "w") as file:
    file.write(f"Nombre: {nombre}\nEdad: {edad}\n")

# Lectura desde archivo
with open("saludo.txt", "r") as file:
    contenido = file.read()

print("\nContenido del archivo 'saludo.txt':")
print(contenido)
