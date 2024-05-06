from UserRequestController import UserRequestController
import functions_framework
#from flask import Flask, request, jsonify

#app = Flask(__name__)

@functions_framework.http

#@app.route('/get_reservation', methods=['GET'])
def get_user_id(request):
    controller = UserRequestController()
    data = request.args

    id_u = data["id"]
    
    response = controller.get_user_id(id_u)
    print(response)
    return response



@functions_framework.http

#@app.route('/add_reservation', methods=['POST'])
def add_user(request):
    controller = UserRequestController()

    data = request.get_json(silent=True)
    
    pw = data['pasword']
    email = data['email']
    name = data['name']
    lname = data['lastname']
    direct = data['direction']
    access = data['access']


    response = controller.add_user(pw, email, name, lname, direct, access)
    return response

@functions_framework.http
#@app.route('/edit_reservation', methods=['POST'])
def login(request):
    controller = UserRequestController()

    #data = request.json  # Obtener los datos del cuerpo de la solicitud JSON

    data = request.get_json(silent=True)
    
    pw = data['pasword']
    email = data['email']

    
    response = controller.login(pw, email)
    return response


@functions_framework.http
def update_password():
    controller = UserRequestController()
    data = request.get_json(silent=True)

    id_u = data['id']
    password = data['pasword']

    response = controller.retrieve_update_password(id_u, pw)
    return response


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
