from UserRequestController import UserRequestController
import functions_framework

# Permite CORS en todas las funciones HTTP
@functions_framework.http
def get_emotions(request):
    controller = UserRequestController()
    text = request.args["text"]
    
    if not text:
        return controller.answer_generator.generate_error_response(460, "Text is empty")

    response = controller.process_emotions(text)
    return response
