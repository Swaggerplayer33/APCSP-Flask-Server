import random
import string

random_code = ''.join(random.choices(string.digits, k=6))

from flask import Flask, request
import random
import string
import os
import sendgrid
from sendgrid.helpers.mail import Mail

# Generate a random code
def generate_random_code():
    return ''.join(random.choices(string.digits, k=6))

# Process the form and send the email
@app.route('/submit', methods=['POST'])
def submit_form():
    user = request.form['user']
    email = request.form['email']

    random_code = generate_random_code()
    message = f"Hello {user}, your code is {random_code}. Show this code when you checkout your car."

    # Send the email using SendGrid
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('08d7639959msh856cfb5944a18fap147283jsnf269b28df190'))
    from_email = sendgrid.helpers.mail.Email("aditya7desai@gmail.com")
    to_email = sendgrid.helpers.mail.Email(email)
    subject = "Your Car Checkout Code"
    content = sendgrid.helpers.mail.Content("text/plain", message)
    mail = sendgrid.helpers.mail.Mail(from_email, subject, to_email, content)
    
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        return "Email sent successfully."
    except Exception as e:
        return f"Email sending failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)