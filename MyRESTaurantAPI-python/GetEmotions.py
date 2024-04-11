from UserRequestController import UserRequestController

controller = UserRequestController()

@app.route("/PostEmotions", methods=["POST"])
def get_emotions():
    text = request.get_json().get("review")

    if not text:
        return jsonify(controller.answer_generator.generate_error_response(460, "Text is empty")), 400

    response = controller.process_emotions(text)
    return jsonify(response), 200