from UserRequestController import UserRequestController
import functions_framework
#from flask import Flask, request, jsonify

#app = Flask(__name__)

@functions_framework.http

#@app.route('/get_reservation', methods=['GET'])
def get_reservation():
    controller = UserRequestController()

    response = controller.get_reservations()
    print(response)
    return response



@functions_framework.http

#@app.route('/add_reservation', methods=['POST'])
def add_reservation(request):
    controller = UserRequestController()

    #data = request.json
    data = request.get_json(silent=True)
    
    #date = request.args["date"]
    #time = request.args["time"]
    #state = request.args["state"]
    
    date = data['date']
    time = data['time']
    state = data['state']
    
    if not date:
        return controller.answer_generator.generate_error_response(460, "Date is empty")
    elif not time:
        return controller.answer_generator.generate_error_response(461, "Time is empty")
    elif not state:
        return controller.answer_generator.generate_error_response(462, "State is empty")

    response = controller.add_reservation(date, time, state)
    return response

@functions_framework.http
#@app.route('/edit_reservation', methods=['POST'])
def edit_reservation(request):
    controller = UserRequestController()
    #id_r = request.args["id"]
    #date = request.args["date"]
    #time = request.args["time"]
    #state = request.args["state"]

    #data = request.json  # Obtener los datos del cuerpo de la solicitud JSON

    data = request.get_json(silent=True)
    
    id_r = data['id']
    date = data['date']
    time = data['time']
    state = data['state']
    
    if not date:
        return controller.answer_generator.generate_error_response(460, "Date is empty")
    elif not time:
        return controller.answer_generator.generate_error_response(461, "Time is empty")
    elif not state:
        return controller.answer_generator.generate_error_response(462, "State is empty")
    elif not id_r:
        return controller.answer_generator.generate_error_response(463, "ID is empty")

    response = controller.edit_reservation(id_r, date, time, state)
    return response


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
