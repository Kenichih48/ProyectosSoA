from ReservationDatabaseControllerMod import ReservationDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:


    def __init__(self):

        self.resDatabaseController = ReservationDatabaseController()
        self.answerGenerator = AnswerGenerator()

    def retrieve_get_res(self):


        reservationJson = self.answerGenerator.generate_success_response(200, self.resDatabaseController.get_current_state())

        return reservationJson

    def retrieve_add_res(self, date, time, state, people_quant, id_user):
        self.resDatabaseController.insert_reservation(date, time, state, people_quant, id_user)
        reservationJson = self.answerGenerator.generate_success_response(200, "")
        return reservationJson

    def retrieve_edit_res(self, id_r, state, people_quant, id_user):

        self.resDatabaseController.edit_reservation(id_r, state, people_quant, id_user)
        reservationJson = self.answerGenerator.generate_success_response(200, "")
        return reservationJson

    def retrieve_get_user(self, id_user):
        
        reservationJson = self.answerGenerator.generate_success_response(200, self.resDatabaseController.getByIdUser(id_user))
        return reservationJson
