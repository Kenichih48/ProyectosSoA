from MenuDatabaseControllerMod import MenuDatabaseController
from ReservationDatabaseControllerMod import ReservationDatabaseController
from AnswerGeneratorMod import AnswerGenerator
import json

class AnswerAdapter:
    """
    Converts responses (dattapull, openai, endpoint) to JSON for our API.
    """

    def __init__(self, file_path1, file_path2):
        """
        Initializes AnswerAdapter with file paths and controllers.

        Parameters:
            file_path1 (str): The file path for menu data.
            file_path2 (str): The file path for reservation data.
        """
        self.file_path1 = file_path1
        self.file_path2 = file_path2
        self.menuDatabaseController = MenuDatabaseController(file_path1)
        self.resDatabaseController = ReservationDatabaseController(file_path2)
        self.answerGenerator = AnswerGenerator()

    def retrieve_data_from_meal_database(self, comida1, tipo1, request, comida2=None, tipo2=None):
        """
        Retrieves data from the meal database based on the provided food and type.

        Parameters:
            comida1 (str): The specified dish, drink, or dessert to search for in the database.
            tipo1 (str): The classification of the requested food (e.g., "dish", "drink", or "dessert").
            request (str): The type of request.
            comida2 (str, optional): The second specified dish, drink, or dessert (required for certain requests).
            tipo2 (str, optional): The classification of the second requested food (required for certain requests).

        Returns:
            str: A JSON string representing the response containing the retrieved data.
        """
        menuItemJson = None

        if request == "0":
            menuItemJson = self.menuDatabaseController.search_full_meal(comida1, tipo1)
        elif request in ["1", "2", "3"]:
            menuItemJson = self.menuDatabaseController.search_single(comida1, tipo1, request, comida2, tipo2)
        else:
            # Invalid request
            return self.answerGenerator.generate_error_response(512, "Invalid request")

        status_code = 512
        errorMessage = "Requested menu item does not exist"

        if menuItemJson == "515":
            status_code = 515
            errorMessage = "Set with both items does not exist"
            menuItemJson = None

        response = self.answerGenerator.generate_success_response(200, menuItemJson) if menuItemJson is not None else self.answerGenerator.generate_error_response(status_code, errorMessage)

        return response

    def retrieve_menu(self):
        """
        Retrieves the menu from the menu database.

        Returns:
            str: A JSON string representing the menu.
        """
        menu = self.menuDatabaseController.get_menu()

        errorCode = 463
        errorMessage = "Menu items are empty"

        response = self.answerGenerator.generate_success_response(200, menu) if menu is not None else self.answerGenerator.generate_error_response(errorCode, errorMessage)

        return json.dumps(response, indent=4)

    def retrieve_data_from_reservation_database(self, date, time):
        """
        Retrieves data from the reservation database based on the provided date and time.

        Parameters:
            date (str): The date of the reservation.
            time (str): The time of the reservation.

        Returns:
            str: A JSON string representing the reservation data.
        """
        reservationJson = self.resDatabaseController.search_best_options(date, time)

        return reservationJson
