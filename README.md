# Python

Python es un lenguaje de programacion de alto nivel, interpretado y multiparadigma. Es conocido por su simplicidad y legibilidad, lo que lo hace accesible tanto para programadores novatos como para expertos. Python es utilizado en una amplia variedad de aplicaciones, desde desarrollo web hasta analisis de datos, inteligencia artificial, automatizacion, y mucho mas. Su sintaxis sencilla y su amplia comunidad de usuarios han contribuido a su popularidad a lo largo de los años.

# En que contexto nacio Python

Python fue creado por Guido van Rossum a finales de los anos 1980 y fue lanzado por primera vez en 1991. Nacio con la intencion de ser un lenguaje que pudiera ser facil de aprender y usar, a la vez que potente y flexible para una variedad de aplicaciones. El lenguaje fue diseñado como una alternativa a lenguajes mas complejos como C y C++ y con un enfoque en la legibilidad del codigo.

# Versiones de Python

Python ha pasado por varias versiones a lo largo de los anos. Algunas de las versiones mas importantes incluyen:

- Python 2.x: Esta version fue ampliamente utilizada, pero ya no recibe soporte desde 2020.
- Python 3.x: Esta es la version actual y la recomendada para el desarrollo nuevo. Introduce varios cambios incompatibles con Python 2, lo que hace que el codigo de Python 2 no sea directamente compatible con Python 3.

## Caracteristicas Principales

- **Bajo o Alto Nivel**: Python es un lenguaje de alto nivel, lo que significa que abstrae detalles complejos del hardware y de la gestion de memoria, permitiendo a los desarrolladores centrarse en la logica del programa.
  
- **Uso de Punteros**: Python no permite el uso directo de punteros como en otros lenguajes como C o C++. La gestion de memoria es automatica mediante un recolector de basura, lo que hace que los punteros no sean necesarios para la mayoria de los casos.

- **Paradigma y Explicacion de los Paradigmas**: Python es un lenguaje multiparadigma, lo que significa que soporta varios enfoques para la programacion. Estos incluyen programacion orientada a objetos, programacion imperativa y programacion funcional. Esto ofrece a los programadores la flexibilidad de elegir el estilo que mejor se adapte a sus necesidades.

- **Tipo de Tipado**: Python es un lenguaje de tipado dinamico, lo que significa que no es necesario declarar el tipo de las variables. El tipo se asigna automaticamente en tiempo de ejecucion segun el valor que se le asigne a la variable.

- **Compilado o Interpretado**: Python es un lenguaje interpretado. Esto significa que el codigo fuente es ejecutado directamente por un interprete sin necesidad de ser compilado previamente a un archivo binario. Esto hace que el desarrollo sea mas rapido, pero tambien puede afectar el rendimiento en algunos casos.

- **Operadores**: Python ofrece una variedad de operadores, incluyendo operadores aritmeticos, logicos, de comparacion y de asignacion. Estos operadores permiten realizar operaciones matematicas, comparaciones y manipular el flujo de control del programa.

# Ejemplos segun paradigma

## POO

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
print(persona1.saludar())
```

## Funcional

```python
# Definicion de una funcion que usa map y filter
def aplicar_funciones(lista):
    # Filtrar los numeros pares y elevarlos al cuadrado
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lista)))

# Usar la funcion con una lista
lista = [1, 2, 3, 4, 5, 6]
print(aplicar_funciones(lista))
```

## Logica

```python
def es_par(x):
    return x % 2 == 0

# Consultas logicas
print(es_par(4))  # True
print(es_par(7))  # False
```

## Imperativo

```python
# Ejemplo de programación imperativa
def suma_imperativa(lista):
    total = 0
    for num in lista:
        total += num
    return total

# Usar la funcion
numeros = [1, 2, 3, 4, 5]
print(suma_imperativa(numeros))
```

# Explicacion de que es pip

pip es el sistema de gestion de paquetes de Python. Permite instalar, actualizar y gestionar librerias de terceros que no forman parte de la biblioteca estandar de Python. pip facilita la descarga e instalacion de paquetes directamente desde el Python Package Index (PyPI), un repositorio en linea que contiene miles de librerias utiles para cualquier tipo de desarrollo en Python.

# Entornos Virtuales en Python

Los entornos virtuales en Python son una forma de aislar las dependencias de un proyecto, evitando conflictos entre las versiones de librerías de diferentes proyectos. Esto permite que cada proyecto tenga su propio conjunto de dependencias sin interferir con otros proyectos o con el sistema global de Python.

## ¿Por qué usar entornos virtuales?

- **Aislamiento de dependencias**: Cada proyecto puede tener sus propias librerías y versiones sin interferir con otros proyectos.
- **Compatibilidad**: Evita problemas de compatibilidad entre diferentes versiones de librerías o de Python.
- **Facilidad de gestión**: Hace que sea más fácil gestionar dependencias cuando se trabaja en proyectos con diferentes requerimientos.

## Creación de un entorno virtual

1. **Instalar `venv`**: Si tienes Python 3.3 o superior, el módulo `venv` ya está incluido en la instalación estándar. Si no está disponible, puedes instalarlo en tu sistema.
   
2. **Crear el entorno virtual**: Dentro de la terminal, navega al directorio de tu proyecto y crea un entorno virtual. Esto generará una carpeta con el nombre del entorno, que contiene una copia aislada de Python y sus herramientas.

```bash
python3 -m venv nombre_del_entorno
```

3. **Activar el entorno virtual**: Para trabajar dentro del entorno, debes activarlo. Esto cambiará el contexto de Python a ese entorno aislado, lo que te permite instalar librerías sin afectar el entorno global.

```bash
nombre_del_entorno\Scripts\activate
```

4. **Instalar dependencias**: Una vez dentro del entorno virtual, puedes instalar las librerías necesarias para tu proyecto utilizando el administrador de paquetes `pip`.

5. **Desactivar el entorno virtual**: Después de trabajar, puedes desactivar el entorno virtual para regresar al entorno global.

```bash
deactivate
```

6. **Usar un archivo de dependencias**: Para compartir las dependencias de tu proyecto o restaurarlas en el futuro, puedes generar un archivo de dependencias que pueda ser usado por otros colaboradores o en otros entornos.

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```
