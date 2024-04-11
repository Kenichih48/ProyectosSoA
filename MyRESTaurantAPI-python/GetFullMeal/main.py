from UserRequestController import UserRequestController


import functions_framework

@functions_framework.http
def get_full_meal(request):
    controller = UserRequestController()
    comida = request.args["comida"]
    tipo = request.args["tipo"]

    if not comida:
        return controller.answer_generator.generate_error_response(453, "Comida is empty")
    elif not tipo:
        return controller.answer_generator.generate_error_response(454, "Tipo is empty")

    response = controller.process_meal(comida, tipo, "0")
    return response
