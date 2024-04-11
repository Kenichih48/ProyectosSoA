from UserRequestController import UserRequestController

controller = UserRequestController()

@app.route("/GetAvailability", methods=["GET"])
def get_availability():
    #controller = UserRequestController()
    date = request.args.get("date")
    time = request.args.get("time")

    if not date:
        return jsonify(controller.answer_generator.generate_error_response(460, "Date is empty")), 400
    elif not time:
        return jsonify(controller.answer_generator.generate_error_response(461, "Time is empty")), 400

    response = controller.process_reservation(date, time)
    return jsonify(response), 200