#from flask import Flask, request, jsonify
from AnswerGeneratorMod import AnswerGenerator
from SentimentFunct.SentimentController import Sentiment

#from UserRequestController import UserRequestController
#app = Flask(__name__)

class UserRequestController:
    """
    Controller to handle user requests.
    """

    def __init__(self):

        self.answer_generator = AnswerGenerator()

    def process_emotions(self, text):

        response = Sentiment.getSentiment(text, 'SentimentFunct/soa-cloud-3f986d1b8bf4.json')
        return self.answer_generator.generate_success_response(200, str(response))

#controller = UserRequestController()




#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
