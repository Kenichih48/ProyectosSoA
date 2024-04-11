from UserRequestController import UserRequestController

controller = UserRequestController()

@app.route("/GetMenu", methods=["GET"])
def get_menu():
    response = controller.process_menu()
    return jsonify(response), 200