from UserRequestController import UserRequestController
import functions_framework
#from flask import Flask, request, jsonify

#app = Flask(__name__)

@functions_framework.http

#@app.route('/getUserId', methods=['GET'])
def get_user_id(request):
    controller = UserRequestController()
    data = request.args

    id_u = data["id"]
    
    response = controller.get_user_id(id_u)
    print(response)
    return response



@functions_framework.http
#@app.route('/addUser', methods=['POST'])
def add_user(request):
    controller = UserRequestController()

    data = request.get_json(silent=True)
    
    pw = data['contrasena']
    email = data['correo']
    name = data['nombre']
    lname = data['apellido']
    direct = data['direccion']
    access = data['nivel_acceso']


    response = controller.add_user(pw, email, name, lname, direct, access)
    return response

@functions_framework.http

#@app.route('/login', methods=['POST'])
def login(request):
    controller = UserRequestController()

    #data = request.json  # Obtener los datos del cuerpo de la solicitud JSON

    data = request.get_json(silent=True)
    
    pw = data['contrasena']
    email = data['correo']

    
    response = controller.login(pw, email)
    return response


@functions_framework.http
#@app.route('/updatePassword', methods=['POST'])
def update_password(request):
    controller = UserRequestController()
    data = request.get_json(silent=True)

    id_u = data['id']
    password = data['contrasena']

    response = controller.update_password(id_u, password)
    return response


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
