from UserRequestController import UserRequestController
#from flask import Flask, request, jsonify


import functions_framework


#app = Flask(__name__)

#@app.route("/GetMenu", methods=["GET"])
@functions_framework.http
def get_menu():
    controller = UserRequestController()
    response = controller.process_menu()
    return response



#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
