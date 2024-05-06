import json

class AnswerGenerator:
    """
    Generates response objects for success and error cases.
    """

    def generate_success_response(self, status_code, input_data):
        """
        Generates a success response object for the given input JSON.

        Parameters:
            status_code (int): The status code for the response.
            input_data (str): The JSON input.

        Returns:
            dict: A success response object containing the input JSON.
        """
        #json_data = json.loads(input_data)

        response = {
            "status_code": status_code,
            "status": "success",
            "data": input_data
        }

        return response

    def generate_error_response(self, status_code, message):
        """
        Generates an error response object.

        Parameters:
            status_code (int): The status code for the response.
            message (str): The error message.

        Returns:
            dict: An error response object.
        """
        response = {
            "status_code": status_code,
            "status": "error",
            "message": message
        }

        return response
