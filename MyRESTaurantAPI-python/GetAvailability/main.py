from UserRequestController import UserRequestController
#from Flask import jsonify
import functions_framework


@functions_framework.http
def get_availability(request):
    controller = UserRequestController()
    date = request.args["date"]
    time = request.args["time"]

    if not date:
        return controller.answer_generator.generate_error_response(460, "Date is empty")
    elif not time:
        return controller.answer_generator.generate_error_response(461, "Time is empty")

    response = controller.process_reservation(date, time)
    return response
