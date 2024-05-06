#from flask import Flask, request, jsonify
from AnswerAdapterMod import AnswerAdapter
from AnswerGeneratorMod import AnswerGenerator


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

    def process_menu(self):
        """
        Processes menu-related requests.
        """
        response = self.answer_adapter.retrieve_menu()
        return response

