from MenuDatabaseControllerMod import MenuDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:
    """
    Converts responses (dattapull, openai, endpoint) to JSON for our API.
    """

    def __init__(self):

        self.menuDatabaseController = MenuDatabaseController()
        self.answerGenerator = AnswerGenerator()

    

    def retrieve_menu(self):

        menu = self.menuDatabaseController.get_menu()

        errorCode = 463
        errorMessage = "Menu items are empty"

        response = self.answerGenerator.generate_success_response(200, menu) if menu is not None else self.answerGenerator.generate_error_response(errorCode, errorMessage)

        return json.dumps(response, indent=4)
