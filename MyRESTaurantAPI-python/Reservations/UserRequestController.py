#from flask import Flask, request, jsonify
from AnswerAdapterMod import AnswerAdapter
from AnswerGeneratorMod import AnswerGenerator

#from UserRequestController import UserRequestController
#app = Flask(__name__)

class UserRequestController:
    """
    Controller to handle user requests.
    """

    def __init__(self):
        """
        Initializes the UserRequestController.
        """
        self.answer_adapter = AnswerAdapter()
        self.answer_generator = AnswerGenerator()


    def get_reservations(self):
        
        response = self.answer_adapter.retrieve_get_res()
        
        return response

    def add_reservation(self, date, time, state):

        response = self.answer_adapter.retrieve_add_res(date, time, state)
        return response

    def edit_reservation(self, id_r, date, time, state):

        response = self.answer_adapter.retrieve_edit_res(id_r, date, time, state)
        return response




#controller = UserRequestController()


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
