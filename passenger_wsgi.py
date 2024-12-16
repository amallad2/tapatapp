import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
import prova
import DAOUser

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
DATABASE_URL = "mysql+pymysql://root:root@localhost/tapatapp"
daoUSer = DAOUser.UserDAO(DATABASE_URL)


@app.route('/')
def index():
    return 'Hello from flask'
    
@app.route('/get_data', methods=['GET'])
def get_data():
    # Example data
    data = {
        "status": "success",
        "message": "This is a JSON response",
        "data": {
            "id": 1,
            "name": "Sample Item"
        }
    }
    # Return JSON response
    return jsonify(data)

@app.route('/prova2', methods=['GET'])
def prova2():
	return prova.provaFunc()

@app.route("/login", methods=["POST"])
def login():
    data = request.json  #Content-Type: application/json
    username = data.get("username")
    password = data.get("password")
    result = daoUSer.login_user(username,password)
    if(result[0] == 1):
        access_token = result[1]
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401

@app.route("/login2", methods=["POST"])
def login2():
    #Content-Type: application/x-www-form-urlencoded
    ## TEST NO VA la petició 
    username = request.form["username"]
    password = request.form["password"]
    print("USER: ", username, password)
    result = daoUSer.login_user(username,password)
    if(result[0] == 1):
        access_token = result[1]
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401

application = app
app.run(debug=True)
