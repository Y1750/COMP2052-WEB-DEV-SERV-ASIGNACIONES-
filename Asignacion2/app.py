from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos en memoria
usuarios = []

# Ruta principal opcional
@app.route("/")
def home():
    return "Servidor Flask en funcionamiento"

# Ruta GET /info
@app.route("/info")
def getInfo():
    sistema = {
        "nombre_sistema": "Gestor Flask",
        "version": "1.0",
        "autor": "Tu Nombre"
    }
    return jsonify(sistema), 200

# Ruta POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crearUsuario():
    data = request.get_json()
    
    nombre = data.get("nombre", "")
    correo = data.get("correo", "")
    
    if not nombre or not correo:
        return jsonify({"error": "Se requiere nombre y correo"}), 400
    
    nuevo_usuario = {
        "nombre": nombre,
        "correo": correo
    }
    
    usuarios.append(nuevo_usuario)
    
    return jsonify({"mensaje": "Usuario creado correctamente", "usuario": nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route("/usuarios")
def obtenerUsuarios():
    return jsonify({"usuarios": usuarios}), 200


if __name__ == "__main__":
    app.run(debug=True)
