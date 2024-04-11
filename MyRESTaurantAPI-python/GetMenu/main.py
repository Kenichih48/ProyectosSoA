from UserRequestController import UserRequestController

import functions_framework

@functions_framework.http
def get_menu(request):
    controller = UserRequestController()
    response = controller.process_menu()
    return response
