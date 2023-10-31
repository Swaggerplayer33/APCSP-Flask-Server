from flask import Flask, Blueprint, request
from flask_restful import Api  # Import Api from Flask-RESTful (if you want to use it)
import random
import string
import sendgrid
from sendgrid.helpers.mail import Mail

# Create a Flask app instance
app = Flask(__name__)

# Create a Blueprint for the email API
email_api = Blueprint('email_api', __name__, url_prefix='/api/email')

# Create the API instance (if you want to use Flask-RESTful)
api = Api(email_api)

# Define the send_email function
def send_email(user, email):
    # Generate a random code
    random_code = ''.join(random.choices(string.digits, k=6))

    # Construct the email message
    message = Mail(
        from_email="aditya7desai@gmail.com",
        to_emails=email,
        subject="Car Checkout Code",
        plain_text_content=f"Hello {user}, your code is {random_code}. Show this code when you checkout your car."
    )

    # Send the email using SendGrid
    sg = sendgrid.SendGridAPIClient(api_key="08d7639959msh856cfb5944a18fap147283jsnf269b28df190")
    sg.send(message)

# Define a route for form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']

        # Check if user and email are provided
        if user and email:
            send_email(user, email)
            return "Email sent successfully."
        else:
            return "User and email are required."

# Run the Flask app
if __name__ == '__main__':
    app.run()

