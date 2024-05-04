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

    def retrieve_add_res(self, date, time, state):
        self.resDatabaseController.insert_reservation(date, time, state)
        reservationJson = self.answerGenerator.generate_success_response(200, "")
        return reservationJson

    def retrieve_edit_res(self, id_r, date, time, state):

        self.resDatabaseController.edit_reservation(id_r, date, time, state)
        reservationJson = self.answerGenerator.generate_success_response(200, "")
        return reservationJson
