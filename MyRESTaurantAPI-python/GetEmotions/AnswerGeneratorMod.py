import json

class AnswerGenerator:
    """
    Generates response objects for success and error cases.
    """

    def generate_success_response(self, status_code, input_data):

        #json_data = json.loads(input_data)

        response = {
            "status_code": status_code,
            "status": "success",
            "data": input_data
        }

        return response

    def generate_error_response(self, status_code, message):

        response = {
            "status_code": status_code,
            "status": "error",
            "message": message
        }

        return response
