# Code used from official Twilio documentation
# Download the module ~ pip3 install twilio
# Download the module ~ pip3 install sendgrid
# Download the module ~ pip3 install email-validator
# Make sure to save your authentication token in your private config.py file 

from twilio.rest import Client
from config import sid, password, phone_number, email_api

import sendgrid
from sendgrid.helpers.mail import *

#Messaging Portion

account_sid = sid
auth_token = password
client = Client(account_sid, auth_token)

def messaging(body, to = "+14159919818", from_ = phone_number):
    message = client.messages.create(
    body = body, 
    to = "+14159919818", 
    from_= phone_number,
    )

# Email Portion
def email_send(email, subject1, content1):
    sg = sendgrid.SendGridAPIClient(email_api)
    from_email = Email("steeljer@oregonstate.edu")
    to_email = To(email)
    subject = subject1
    content = Content("text/plain", content1)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code


