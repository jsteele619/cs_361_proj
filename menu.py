from message import messaging, email_send
import time
import zmq
from email_validator import validate_email, EmailNotValidError



def menu():

    print("\nWelcome to the Text Messaging Application \n" )
    print(" - To send a text message, press 1 then enter.")
    print(" - To send an email, press 2 then enter.")
    print(" - To see more options, press 3 then enter.")
    print(" - To return to the main menu, press h then enter at any time.")
    print(" - To quit this application, press q then enter.")

    key_press = input()
    while key_press:
        if key_press == "1":
            key_press = False
            text_message()
        elif key_press == "2":
            key_press = False
            email()
        elif key_press == "3": 
            key_press = False
            more_options() 
        elif key_press == "h":
            key_press = False
            menu()
        elif key_press == "q":
            return
        else:
            print("Please try again. That wasn't a valid input.")
            key_press = input()
            
def text_message():
    wants_continue = True
    while wants_continue:
        print("\n Please enter a phone number below as one string of numbers like this: 1234567890")
        phone_num = input()
        if return_to_menu(phone_num):
            wants_continue = False
            menu()
        if check_number(phone_num) is False:
            print("That wasn't a valid ten digit number. ")
            continue
        print("You entered: " + phone_num)
        print("Is that correct? Press 1 for yes, 2 for no.")
        key_num = input()
        if key_num == "1":
            wants_continue = False
        if return_to_menu(phone_num):
            wants_continue = False
            menu()

    new_cond = True
    while new_cond: 
        print("\nPlease type your message and press enter when finished.")
        message = input()
        print("\nPress 1 to send. Press 2 to edit. Press 3 to translate. Press h for more options.")
        key_num = input()
        if key_num == "1":
            new_cond = False
            phone_num = "+1" + phone_num
            receive = "+14159919818"
            try:
                messaging(message)  # body, to = "+14159919818", from_ = phone_number
                print("Message sent. Thank you")
                new_cond = False
                menu()
            except Exception as e:
                print("An error has occured: " + e)
                print("/n Please try again")
                new_cond = False
                menu()
        elif key_num == "2":
            continue
        elif key_num == "3":
            translation = comm_translate(message, "German")
            print(translation)
            print("\nPress 1 to send. Press 2 to edit. Press h for more options.")
            key_num = input()
            if key_num == "1":
                new_cond = False
                try:
                    messaging(translation)  # body, to = "+14159919818", from_ = phone_number
                    print("Message sent. Thank you")
                    new_cond = False
                    menu()
                except Exception as e:
                    print("An error has occured: ")
                    print(e)
                    print("/n Please try again")
                    new_cond = False
                    menu()
            elif key_num == "2":
                continue
            elif return_to_menu(key_num):
                new_cond = False
                menu()
            else:
                print("Your input wasn't accepted.")
                continue
        elif return_to_menu(key_num):
            new_cond = False
            menu()
        else:
            print("\nYour input wasn't accepted.")
            continue 

def email():
    value = True
    while value:
        print("\nPlease enter a valid email address")
        email = input()
        if return_to_menu(email):
            value = False
            menu()
        try:                                                                # Check that the email address is valid.
            validation = validate_email(email, check_deliverability=True)
        except EmailNotValidError as e:
            print(str(e))
            continue
        print("\nYou entered: " + email)
        print("Is that correct? Press 1 for yes, 2 for no.")
        key_num = input()
        if key_num == "1":
            value = False
        if return_to_menu(email):
            value = False
            menu()
    
    new_value = True
    while new_value:
        print("\nPlease type your subject message and press enter when finished.")
        subject = input()
        print("\nPress 1 to continue. Press 2 to edit. Press 3 to translate.")
        key_num = input()
        if key_num == "1":
            new_value = False
        elif key_num == "2":
            continue
        elif key_num == "3":
            subject = comm_translate(subject, "German")
            print("Your translation: " + subject)
        elif return_to_menu(key_num):
            new_value = False
            menu()
        new_value = False
    
    newer_val = True
    while newer_val:
        print("\nPlease type your content message and press enter when finished.")
        content = input()
        print("\nPress 1 to continue. Press 2 to edit. Press 3 to translate.")
        key_num = input()
        if key_num == "1":
            newer_val = False
        elif key_num == "2":
            continue
        elif key_num == "3":
            content = comm_translate(content, "German")
            print("Your translation: " + content)
        elif return_to_menu(key_num):
            newer_val = False
            menu()
        newer_val = False
    print("\nEmail Review")
    print("  Recipient: " + email)
    print("  Subject Line: " + subject)
    print("  Message Content: " + content)
    print("\nIf correct, press 1 to send. If not, press h to return to main menu")

    key_number = input()
    if key_number == "1":
        try:
            email_send(email, subject, content)
            print("\nEmail sent. Thank you")
            menu()
        except Exception as e:
            print("An error has occured: " + e)
            print("/n Please try again")
            menu()

def comm_translate(text, lang):

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5545")

    socket.send_json({'lang': lang, 'text': text})
    time.sleep(.5)
    message = socket.recv_json()
    socket.close()
    return message['text']

def more_options():
    print("There are no more options.")
    menu()
    return

def check_number(num):
    if len(num) != 10:
        return False
    if num.isdigit() == False:
        return False
    return True

    if len(num) != 4:
        return False
    if num.isdigit() == False:
        return False
    return True

def return_to_menu(char):
    if char == "h":
        return True

def new_username(user):
    """ Check if username exists already, return True if its a new username """
    return True






