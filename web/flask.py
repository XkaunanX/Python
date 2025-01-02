# flask_basico.py

from flask import Flask, render_template

# Crear la app de Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "¡Hola, Mundo!"

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
