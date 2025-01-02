# rest_api.py

from flask import Flask, request, jsonify

# Crear la app de Flask
app = Flask(__name__)

# Datos de ejemplo (normalmente se usaría una base de datos)
datos = [
    {"id": 1, "nombre": "Juan", "edad": 30},
    {"id": 2, "nombre": "Ana", "edad": 25}
]

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(datos)

# Ruta para agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    nuevo_usuario = request.get_json()
    datos.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
