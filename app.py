from flask import Flask

app = Flask(__name__)

# Obtén el puerto desde la variable de entorno PORT, o usa 8080 por defecto
port = 8080

@app.route('/')
def hello():
    return '¡Hola Mundo!'

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en el puerto especificado
    app.run(host='0.0.0.0', port=port)
