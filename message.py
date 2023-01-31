# Code used from official Twilio documentation
# Download the helper library ~ pip3 install twilio
# Make sure to save your authentication token in your private config.py file by
# creating a local .gitignore file and writing config.py in it

import os
from twilio.rest import Client
from config import sid, password, phone_number

account_sid = sid
auth_token = password
client = Client(account_sid, auth_token)


def messaging(send, receive, body):
    message = client.messages.create(
    body = body, 
    to = "+14159919818", 
    from_= phone_number,
    )

        