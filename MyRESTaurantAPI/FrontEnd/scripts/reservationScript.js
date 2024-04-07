import { ROOT } from './variables.js';

const reservationForm = document.getElementById('reservation-form');
const reservationMessage = document.getElementById('reservation-message');

reservationForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const date = formData.get('date');
  const time = formData.get('time');

  try {
    // Generar la URL con los parámetros
    const url = new URL(`${ROOT}/GetAvailability`);
    url.searchParams.append('date', date);
    url.searchParams.append('time', time);

    // Realizar la solicitud GET al Backend Cloud Function
    const response = await fetch(url, {
        method: 'POST'
    });

    if (response.ok) {
        const responseData = await response.json();
        if (responseData.status_code === 200) {
            reservationMessage.textContent = 'Reservation date and time is available';
            reservationMessage.style.color = 'green';
        } else if (responseData.status_code === 201) {
            const data = responseData.data;
            let message = 'The selected date and time for the reservation is occupied\n We recommend the following dates and times based on your search: \n';
            data.forEach(timeSlot => {
                message += `&middot&nbsp;&nbsp;${timeSlot.Date} ${timeSlot.Time}\n`;
            })
            reservationMessage.innerHTML = message;

            reservationMessage.style.color = 'red';
        } else {
            reservationMessage.textContent = `Error: ${responseData.message}`;
            reservationMessage.style.color = 'red';
        }
      } else {
        // Manejar el caso en el que la respuesta no es 'ok'
        const error = await response.text();
        reservationMessage.textContent = `Error: ${error}`;
        reservationMessage.style.color = 'red';
      }
      
  } catch (error) {
    reservationMessage.textContent = `Error: ${error.message}`;
    reservationMessage.style.color = 'red';
  }
});