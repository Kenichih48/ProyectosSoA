import json

class MenuDatabaseController:
    """
    Controller for accessing menu data.
    """

    def __init__(self, file_path):
        """
        Initializes MenuDatabaseController with the file path.

        Parameters:
            file_path (str): The file path for the menu data.
        """
        self.file_path = file_path

    def search_full_meal(self, comida, tipo):
        """
        Searches for a full meal in the database based on the provided food and type.

        Parameters:
            comida (str): The type of food to search for in the database.
            tipo (str): The type of information to retrieve (e.g., "dish", "drink", or "dessert").

        Returns:
            str: A JSON string representing the retrieved data of the menu item.
        """
        with open(self.file_path, 'r') as file:
            menu_data = json.load(file)

            matching_menu = next((menu for menu in menu_data if menu.get(tipo.lower()) == comida), None)

            if matching_menu:
                menu_item = {}
                for key, value in matching_menu.items():
                    if key != tipo.lower() and value:
                        menu_item[key] = value

                return menu_item

            return None

    def get_menu(self):
        """
        Retrieves the entire menu.

        Returns:
            str: A JSON string representing the entire menu.
        """
        with open(self.file_path, 'r') as file:
            menu_data = json.load(file)

            if menu_data:
                return menu_data

            return None

    def search_single(self, comida1, tipo1, request, comida2=None, tipo2=None):
        """
        Searches for a single menu item based on provided parameters.

        Parameters:
            comida1 (str): The first food item to search for.
            tipo1 (str): The type of the first food item.
            request (str): The type of request.
            comida2 (str, optional): The second food item to search for.
            tipo2 (str, optional): The type of the second food item.

        Returns:
            str: A JSON string representing the retrieved menu item.
        """
        with open(self.file_path, 'r') as file:
            menu_data = json.load(file)

            matching_menu = None
            set_exists = True

            if not (comida2 and tipo2):  # If only one parameter is provided
                matching_menu = next((menu for menu in menu_data if menu.get(tipo1.lower()) == comida1), None)
            else:  # If two parameters are provided
                if tipo2:
                    tipo1, tipo2 = tipo1.lower(), tipo2.lower()

                possible_queries = [(tipo1, tipo2), (tipo2, tipo1)]

                for t1, t2 in possible_queries:
                    matching_menu = next((menu for menu in menu_data if menu.get(t1) == comida1 and menu.get(t2) == comida2), None)
                    if matching_menu:
                        break

                if not matching_menu:
                    set_exists = False

            response = None

            if matching_menu and set_exists:
                response = matching_menu.get(request.lower())

            if not response and set_exists:
                return None

            if not set_exists:
                return "515"

            return {"response": response}
