#from flask import Flask, request, jsonify
from AnswerAdapterMod import AnswerAdapter
from AnswerGeneratorMod import AnswerGenerator

#from UserRequestControllerMod import UserRequestController
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


    def get_user_id(self, id_u):
        
        response = self.answer_adapter.retrieve_get_id(id_u)
        
        return response

    def add_user(self, pw, email, name, lname, direct, access):

        response = self.answer_adapter.retrieve_add_user(pw, email, name, lname, direct, access)
        return response

    def login(self, pw, email):

        response = self.answer_adapter.retrieve_login(pw, email)
        return response

    def update_password(self, id_u, pw):

        response = self.answer_adapter.retrieve_update_password(id_u, pw)
        return response



#controller = UserRequestController()


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8777)
