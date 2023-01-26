from message import send_message


def menu():

    print("\nWelcome to the Text Messaging Application \n" )

    print(" - To send a text message, press 1 then enter.")
    print(" - To send an email, press 2 then enter.")
    print(" - To Log In to your account, press 3 then enter.")
    print(" - To Sign up a new account, press 4 then enter.")
    print(" - To see more options, press 5 then enter.")
    print(" - To return to the main menu, press h then enter at any time.")
    
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
            login()
        elif key_press == "4":
            key_press = False
            sign_up()
        elif key_press == "5": 
            key_press = False
            more_options() 
        elif key_press == "h":
            key_press = False
            menu()
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
        if return_to_menu(phone_num):
            new_cond = False 
            menu()
        print("\nPress 1 to send. Press 2 to edit. Press h for more options.")
        key_num = input()
        if key_num == "1":
            new_cond = False
            send_message(phone_num, message)
        elif key_num == "2":
            continue
        elif return_to_menu(key_num):
            new_cond = False
            menu()    

def email():
    return


def sign_up():
    print("\nWelcome to our signup menu:")
    cond = True
    while cond:
        print("Please enter a new username")
        new_user = input()
        if new_username(new_user) == False:
            print("That username is already taken.")
            continue
        if return_to_menu(new_user):
            cond = False
            menu()
        cond = False
    
    cond = True
    while cond:
        print("\nPlease enter a 4 digit pin number")
        four = input()
        if check_four(four) != True:
            print("That was either not 4 digits or not a number.")
            continue
        if return_to_menu(four):
            cond = False
            menu()
        sign_up_backend(new_user, four)
        print("You are now logged in as: " + new_user)
        cond = False
    signed_menu()
    return

def login():
    print("\n You are in the Log In menu.")
    
    cond = True
    new_cond = True
    count = 0

    while cond:
        print("Please enter your username:")
        user = input()
        if new_username(user) != True:
            print("That username is incorrect.")
            continue
        if return_to_menu(user):
            cond = False
            menu()
        while new_cond:
            print("Please enter your pin.")
            pin = input()
            if return_to_menu(pin):
                cond, new_cond = False, False
                menu()
            if check_four(pin) is False:
                count +1
                print("That pin was incorrect\n")
                if count == 3:
                    print("You have entered your pin too many times. Return to the main menu.")
                    cond, new_cond = False, False
                    menu()
                continue
            if login_check(user, pin) is False:
                count +1
                print("That pin was incorrect")
                if count == 3:
                    print("You have entered your pin too many times. Return to the main menu.")
                    cond, new_cond = False, False
                    menu()
                continue
            
            cond, new_cond = False, False
            login_backend(user, pin)
        return

def more_options():
    print("There are no more options.")
    menu()
    return

def signed_menu():
    return

def sign_up_backend(new_user, pin):
    return True

def login_backend(user, pin):
    return

def login_check(user, pin):
    return True

def check_number(num):
    if len(num) != 10:
        return False
    if num.isdigit() == False:
        return False
    return True
def check_four(num):
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







