import json

class ReservationDatabaseController:
    """
    Controller for accessing reservation data.
    """

    def __init__(self, file_path):
        """
        Initializes ReservationDatabaseController with the file path.

        Parameters:
            file_path (str): The file path for the reservation data.
        """
        self.file_path = file_path

    def search_best_options(self, date, time):
        """
        Searches for the best reservation options based on the provided date and time.

        Parameters:
            date (str): The date of the reservation.
            time (str): The time of the reservation.

        Returns:
            str: A JSON string representing the best reservation options.
        """
        with open(self.file_path, 'r') as file:
            reservations_data = json.load(file)

            exact_match = next((res for res in reservations_data if res.get("Date") == date and res.get("Time") == time and res.get("State") == "Free"), None)

            if not exact_match:
                not_exact_match = [res for res in reservations_data if (res.get("Date") == date or res.get("Time") == time) and res.get("State") == "Free"]
                if not not_exact_match:
                    return {"status_code": 462, "status": "error", "message": "Invalid date or time"}
                else:
                    res_items = [{"Date": res["Date"], "Time": res["Time"]} for res in not_exact_match]
                    res_items_json = res_items
                    return {"status_code": 201, "status": "success", "data": res_items_json}
            else:
                exact_match["State"] = "Taken"
                exact_match_json = [exact_match]
                return {"status_code": 200, "status": "success", "data": exact_match_json}
