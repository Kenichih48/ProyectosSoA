// Función para enviar un comentario al Backend Cloud Function
async function submitFeedback() {
  const feedbackInput = document.getElementById('feedback-input');
  const feedback = feedbackInput.value.trim();

  if (feedback === '') {
    showFeedbackResponse('Por favor, ingresa un comentario.', 'red');
    return;
  }

  try {
    const response = await fetch('/api/feedback', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ feedback }),
    });

    if (response.ok) {
      const data = await response.json();
      showFeedbackResponse(data.message, 'green');
      feedbackInput.value = '';
    } else {
      const error = await response.text();
      showFeedbackResponse(`Error: ${error}`, 'red');
    }
  } catch (error) {
    showFeedbackResponse(`Error: ${error.message}`, 'red');
  }
}

// Función para mostrar respuestas de comentarios
function showFeedbackResponse(message, color) {
  const feedbackResponse = document.getElementById('feedback-response');
  feedbackResponse.textContent = message;
  feedbackResponse.style.color = color;
}

// Inicializar la aplicación
function init() {
  const feedbackSubmit = document.getElementById('feedback-submit');
  feedbackSubmit.addEventListener('click', submitFeedback);
}

init();