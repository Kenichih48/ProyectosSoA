from UsuariosDatabaseControllerMod import UsuariosDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.userDatabaseController = UsuariosDatabaseController()
        self.answerGenerator = AnswerGenerator()

    def retrieve_get_id(self, id_u):

        userJson = self.answerGenerator.generate_success_response(200, self.userDatabaseController.get_id(id_u))

        return userJson

    def retrieve_add_user(self, pw, email, name, lname, direct, access):
        idSend = self.userDatabaseController.insert_user(pw, email, name, lname, direct, access)
        userJson = self.answerGenerator.generate_success_response(200, idSend)
        return userJson

    def retrieve_login(self, pw, email):

        idSend = self.userDatabaseController.login(pw, email)
        userJson = self.answerGenerator.generate_success_response(200, idSend)
        return userJson
    
    def retrieve_update_password(self, id_u, pw):

        self.userDatabaseController.update_password(id_u, pw)
        userJson = self.answerGenerator.generate_success_response(200, "")
        return userJson
