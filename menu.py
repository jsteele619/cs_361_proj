from message import send_message


def menu():

    print("\nWelcome to the Text Messaging Application \n" )

    print(" - To send a text message, press 1 then enter.")
    print(" - To send an email, press 2 then enter.")
    print(" - To Log In to your account, press 3 then enter.")
    print(" - To Sign up a new account, press 4 then enter.")
    print(" - To see more options, press 4 then enter.")
    print(" - To return to the main menu, press h then enter at any time.")
    
    key_press = input()
    while key_press:
        if key_press == "1":
            text_message()
            key_press = False
        elif key_press == "2":
            email()
            key_press = False
        elif key_press == "3":
            login()
            key_press = False
        elif key_press == "4": 
            more_options() 
            key_press = False
        elif key_press == "h":
            menu()
            key_press = False
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
        if check_number(key_num) is False:
            print("That wasn't a number")
        print("You entered: " + phone_num)
        print("Is that correct? Press 1 for yes.")
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
        if return_to_menu(phone_num):
            new_cond = False 
            menu()
        print("\nPress 1 to send. Press 2 to edit. Press h for more options.")
        key_num = input()
        if key_num == "1":
            new_cond = False
            send_message(phone_num, message)
        elif key_num == "2":

        elif return_to_menu(key_num):
            new_cond = False
            menu()    



def email():
    return


def sign_up():


def login():
    print("\n You are in the Log In menu.")
    print("Please enter")
    return

def more_options():
    return


def check_number(num):
    if len(num) != 10:
        return False
    if num.isdigit() == False:
        return False
    return True


def return_to_menu(char):
    if char == "h":
        return True