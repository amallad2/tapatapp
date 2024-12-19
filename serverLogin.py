# pip install flask-jwt-extended
# pip install flask

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)

users = {"user1": "password1", "user2": "password2"}

@app.route('/prova', methods=['GET'])
def prova():
    return "HOLA"


@app.route('/login2', methods=['GET'])
def login2():
    dades = [
        {"id": 1, "nom": "Usuari 1", "email": "usuari1@example.com", "rol": "administrador"},
        {"id": 2, "nom": "Usuari 2", "email": "usuari2@example.com", "rol": "editor"},
        {"id": 3, "nom": "Usuari 3", "email": "usuari3@example.com", "rol": "visor"},
    ]
    return jsonify(dades), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    username=request.headers.get("Username")
    print(username)
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Content-Type: application/x-www-form-urlencoded
@app.route("/provapost", methods=["POST"])
def provapost():
    username = request.form.get('username')  
    print(request.form.listvalues)
    return jsonify(username), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
