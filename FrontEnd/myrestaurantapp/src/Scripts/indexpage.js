import React, { Component } from "react";
import '../Styles/indexStyle.css';
import Header from "./Header.js";

class IndexPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            feedback: "",
            feedbackResponse: "",
            responseColor: ""
        };
    }
    mapScoreToEmoji = (score) => {
        if (score >= 5) {
          return "😄"; // Very Happy
        } else if (score >= 4) {
          return "😊"; // Happy
        } else if (score >= 3) {
          return "😐"; // Neutral
        } else if (score >= 2) {
          return "😕"; // Sad
        } else {
          return "😢"; // Very Sad
        }
      };

      
    submitFeedback = async () => {
        const { feedback } = this.state;

        if (feedback.trim() === "") {
            this.showFeedbackResponse('Please enter a comment.', 'red');
            return;
        }

        try {
            const response = await fetch(`https://us-central1-soa-cloud.cloudfunctions.net/get_emotions?text=${encodeURIComponent(feedback)}`);
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            const data = await response.json();
            
            const emotion = this.mapScoreToEmoji(data.data);
            if (data.status_code === 200) {
              this.showFeedbackResponse(emotion, 'green');
            }
          } catch (error) {
            console.error('Error fetching emotions:', error);
          }
          
    };

    showFeedbackResponse = (message, color) => {
        this.setState({ feedbackResponse: message, responseColor: color });
    };

    handleInputChange = (e) => {
        this.setState({ feedback: e.target.value });
    };

    render() {
        const { feedback, feedbackResponse, responseColor } = this.state;

        return (
            <div className="IndexPage">
                <Header>
                </Header>

                <main>
                    <section id="welcome">
                        <h1>Welcome to My Restaurant</h1>
                        <p>Enjoy our delicious food and drinks!</p>
                    </section>

                    <section id="feedback">
                        <h2>Feedback</h2>
                        <textarea 
                            id="feedback-input" 
                            placeholder="Leave your comment here"
                            value={feedback}
                            onChange={this.handleInputChange}
                        ></textarea>
                        <button id="feedback-submit" onClick={this.submitFeedback}>Send Feedback</button>
                        <div id="feedback-response" style={{ color: responseColor }}>{feedbackResponse}</div>
                    </section>
                </main>

                <footer>
                    <p>&copy; My RESTaurant</p>
                </footer>
            </div>
        );
    }
}

export default IndexPage;
