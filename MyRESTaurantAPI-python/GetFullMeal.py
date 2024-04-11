from UserRequestController import UserRequestController

controller = UserRequestController()

@app.route("/GetFullMeal", methods=["GET"])
def get_full_meal():
    comida = request.args.get("comida")
    tipo = request.args.get("tipo")

    if not comida:
        return jsonify(controller.answer_generator.generate_error_response(453, "Comida is empty")), 400
    elif not tipo:
        return jsonify(controller.answer_generator.generate_error_response(454, "Tipo is empty")), 400

    response = controller.process_meal(comida, tipo, "0")
    return jsonify(response), 200