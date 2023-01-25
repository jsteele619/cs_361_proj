from message import send_message


def menu():
    print("Welcome to the Text Messaging Application")
    print("To send a text message, press 1 then enter.")
    print("To send an email, press 2 then enter.")
    print("To Log In to your account, press 3 then enter.")
    print("To see more options, press 4 then enter.")
    print("To return to the main menu, press h then enter when prompted.")

    key_press = input()
    if key_press == 1:
        text_message()
    elif key_press == 2:
        email()
    elif key_press == 3:
        login()
    elif key_press == 4: 
        more_options()


def text_message():
    print("You pressed 1 to send a text message")
    wants_continue = True

    while wants_continue:

        print("Please enter a phone number below as one string of numbers like this: 1234567890")
        phone_num = input()
        print("You entered: " + phone_num)
        print("Is that correct? Press 1 for yes.")
        key_num = input()
        if key_num == 1:
            wants_continue = False
        
    while wants_continue is False: 
        print("Please type your message and press enter when finished.")
        message = input()
        print(message + ": This is your message. Press 1 to send. Press 2 to edit. Press h for more options.")
        key_num = input()
        if key_num == 1:
            wants_continue = True
            send_message(phone_num, message)
        elif key_num == "h":
            wants_continue = True
            more_options()


def email():
    return


def login():
    return

def more_options():
    return