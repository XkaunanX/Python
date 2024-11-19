from flask import Flask

# Crear una instancia de Flask
app = Flask(__name__)

# Definir una ruta que responderá a la URL '/'
@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

# Definir otra ruta para una página de contacto
@app.route('/contacto')
def contacto():
    return 'Página de contacto'

# Arrancar el servidor en el puerto 5000
if __name__ == "__main__":
    app.run(debug=True)