from flask import Flask, request, jsonify
from AnswerAdapterMod import AnswerAdapter
from AnswerGeneratorMod import AnswerGenerator
from SentimentFunct.SentimentController import Sentiment


app = Flask(__name__)

class UserRequestController:
    """
    Controller to handle user requests.
    """

    def __init__(self):
        """
        Initializes the UserRequestController.
        """
        self.answer_adapter = AnswerAdapter("MealDataBase.json", "ReservationDataBase.json")
        self.answer_generator = AnswerGenerator()

    def process_meal(self, comida1, tipo1, request, comida2=None, tipo2=None):
        """
        Processes meal-related requests.
        """
        response = self.answer_adapter.retrieve_data_from_meal_database(comida1, tipo1, request, comida2, tipo2)
        return response

    def process_reservation(self, date, time):
        """
        Processes reservation-related requests.
        """
        response = self.answer_adapter.retrieve_data_from_reservation_database(date, time)
        return response

    def process_menu(self):
        """
        Processes menu-related requests.
        """
        response = self.answer_adapter.retrieve_menu()
        return response

    def process_emotions(self, text):
        """
        Process emotion related requests
        """
        response = Sentiment.getSentiment(text, 'SentimentFunct/soa-cloud-3f986d1b8bf4.json')
        return self.answer_generator.generate_success_response(200, "Scale:" + str(response))

controller = UserRequestController()


@app.route("/PostEmotions", methods=["POST"])
def get_emotions():
    text = request.get_json().get("review")

    if not text:
        return jsonify(controller.answer_generator.generate_error_response(460, "Text is empty")), 400

    response = controller.process_emotions(text)
    return jsonify(response), 200




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

@app.route("/GetDessert", methods=["GET"])
def get_dessert():
    comida1 = request.args.get("comida1")
    tipo1 = request.args.get("tipo1")
    comida2 = request.args.get("comida2")
    tipo2 = request.args.get("tipo2")

    if not comida1:
        return jsonify(controller.answer_generator.generate_error_response(453, "Comida1 is empty")), 400
    elif not tipo1:
        return jsonify(controller.answer_generator.generate_error_response(454, "Tipo1 is empty")), 400
    elif comida2 and not tipo2:
        return jsonify(controller.answer_generator.generate_error_response(455, "Tipo2 is empty while Comida2 is not")), 400
    elif not comida2 and tipo2:
        return jsonify(controller.answer_generator.generate_error_response(456, "Comida2 is empty while Tipo2 is not")), 400

    response = controller.process_meal(comida1, tipo1, "1", comida2, tipo2)
    return jsonify(response), 200

@app.route("/GetDish", methods=["GET"])
def get_dish():
    comida1 = request.args.get("comida1")
    tipo1 = request.args.get("tipo1")
    comida2 = request.args.get("comida2")
    tipo2 = request.args.get("tipo2")

    if not comida1:
        return jsonify(controller.answer_generator.generate_error_response(453, "Comida1 is empty")), 400
    elif not tipo1:
        return jsonify(controller.answer_generator.generate_error_response(454, "Tipo1 is empty")), 400
    elif comida2 and not tipo2:
        return jsonify(controller.answer_generator.generate_error_response(455, "Tipo2 is empty while Comida2 is not")), 400
    elif not comida2 and tipo2:
        return jsonify(controller.answer_generator.generate_error_response(456, "Comida2 is empty while Tipo2 is not")), 400

    response = controller.process_meal(comida1, tipo1, "2", comida2, tipo2)
    return jsonify(response), 200

@app.route("/GetDrink", methods=["GET"])
def get_drink():
    comida1 = request.args.get("comida1")
    tipo1 = request.args.get("tipo1")
    comida2 = request.args.get("comida2")
    tipo2 = request.args.get("tipo2")

    if not comida1:
        return jsonify(controller.answer_generator.generate_error_response(453, "Comida1 is empty")), 400
    elif not tipo1:
        return jsonify(controller.answer_generator.generate_error_response(454, "Tipo1 is empty")), 400
    elif comida2 and not tipo2:
        return jsonify(controller.answer_generator.generate_error_response(455, "Tipo2 is empty while Comida2 is not")), 400
    elif not comida2 and tipo2:
        return jsonify(controller.answer_generator.generate_error_response(456, "Comida2 is empty while Tipo2 is not")), 400

    response = controller.process_meal(comida1, tipo1, "3", comida2, tipo2)
    return jsonify(response), 200

@app.route("/GetMenu", methods=["GET"])
def get_menu():
    response = controller.process_menu()
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)
