from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/users/<userId>")
def getUser(userId):
    user = {"id": userId, "name": "test", "telefono": "999-666-333"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200 

@app.route("/users", methods=["POST"])
def createUser():
    data = request.get_json()
    edad = data.get("edad", "")
    return jsonify({"edad": edad}), 201


@app.route("/info", methods=["GET"])
def get_info():
    info = {
        "app": "Flask Basic Server",
        "version": "1.0",
        "author": "Your Name"
    }
    return jsonify(info), 200

@app.route("/mensaje", methods=["POST"])
def receive_message():
    data = request.get_json()
    mensaje = data.get("mensaje", "")
    response = {
        "respuesta": f"Message received: {mensaje}"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
