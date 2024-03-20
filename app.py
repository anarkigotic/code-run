from flask import Flask , jsonify

app = Flask(__name__)

# Obtén el puerto desde la variable de entorno PORT, o usa 8080 por defecto
port = 8080


# Nueva ruta para obtener la lista de usuarios falsos
@app.route('/usuarios')
def obtener_usuarios():
    # Lista de usuarios falsos
    usuarios_falsos = [
        {"id": 1, "nombre": "Juan", "edad": 25},
        {"id": 2, "nombre": "María", "edad": 30},
        {"id": 3, "nombre": "Pedro", "edad": 28}
    ]
    return jsonify(usuarios_falsos)

@app.route('/ciudades')
def obtener_usuarios():
    # Lista de usuarios falsos
    usuarios_falsos = [
        {"id": 1, "nombre": "Juan", "edad": 25},
        {"id": 2, "nombre": "María", "edad": 30},
        {"id": 3, "nombre": "Pedro", "edad": 28}
    ]
    return jsonify(usuarios_falsos)


@app.route('/')
def hello():
    return '¡Hola Mundo!'

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en el puerto especificado
    app.run(host='0.0.0.0', port=port)
