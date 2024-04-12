import React, { Component } from "react";
import '../Styles/reservationStyle.css'
import Header from "./Header.js";

class ReservPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event) {
        event.preventDefault();

        const formData = new FormData(event.target);
        const date = formData.get('date');
        const time = formData.get('time');

        try {
            // Generate the URL with parameters
            const url = new URL(`https://us-central1-soa-cloud.cloudfunctions.net/get_availability`);
            url.searchParams.append('date', date);
            url.searchParams.append('time', time);

            // Perform the POST request to the Cloud Function backend
            const response = await fetch(url, {
                method: 'POST'
            });

            if (response.ok) {
                const responseData = await response.json();
                if (responseData.status_code === 200) {
                    this.setState({ message: 'Reservation date and time is available' });
                } else if (responseData.status_code === 201) {
                    const data = responseData.data;
                    let message = 'The selected date and time for the reservation is occupied\n We recommend the following dates and times based on your search: \n';
                    data.forEach(timeSlot => {
                        message += `· ${timeSlot.Date} ${timeSlot.Time}\n`;
                    })
                    this.setState({ message });
                } else {
                    this.setState({ message: `Error: ${responseData.message}` });
                }
            } else {
                // Handle non-ok response
                const error = await response.text();
                this.setState({ message: `Error: ${error}` });
            }
        } catch (error) {
            this.setState({ message: `Error: ${error.message}` });
        }
    }
    

    render() {
        return (
            <div className="ReservPage">
                <Header/>
                <div className="container">
                    <h1>Make a Reservation</h1>
                    <form onSubmit={this.handleSubmit} id="reservation-form">
                        <div className="form-group">
                            <label htmlFor="date">Date:</label>
                            <select id="date" name="date" required>
                                <option value="">Choose a date</option>
                                <option value="Monday">Monday</option>
                                <option value="Tuesday">Tuesday</option>
                                <option value="Wednesday">Wednesday</option>
                                <option value="Thursday">Thursday</option>
                                <option value="Friday">Friday</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label htmlFor="time">Time:</label>
                            <select id="time" name="time" required>
                                <option value="">Choose a time</option>
                                <option value="13:00">13:00</option>
                                <option value="14:00">14:00</option>
                                <option value="15:00">15:00</option>
                                <option value="16:00">16:00</option>
                                <option value="17:00">17:00</option>
                            </select>
                        </div>
                        <button type="submit">Check Availability</button>
                    </form>
                    <pre id="reservation-message">{this.state.message}</pre>
                </div>
            </div>
        );
    }
}

export default ReservPage;
