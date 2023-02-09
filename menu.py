from message import messaging
import time
import zmq

class User:
    def __init__(self) -> None:
        self.message
        self.phone_num
        self.user_name
        self.pin
        address_book = {}
        self.address_book = address_book
        pass

    def menu(self):

        print("\nWelcome to the Text Messaging Application \n" )

        print(" - To send a text message, press 1 then enter.")
        print(" - To send an email, press 2 then enter.")
        print(" - To Log In to your account, press 3 then enter.")
        print(" - To Sign up a new account, press 4 then enter.")
        print(" - To see more options, press 5 then enter.")
        print(" - To return to the main menu, press h then enter at any time.")
        print(" - To quit this application, press q then enter.")
        
        user = User()

        key_press = input()
        while key_press:
            if key_press == "1":
                key_press = False
                self.text_message()
            elif key_press == "2":
                key_press = False
                self.email()
            elif key_press == "3":
                key_press = False
                self.login()
            elif key_press == "4":
                key_press = False
                self.sign_up()
            elif key_press == "5": 
                key_press = False
                self.more_options() 
            elif key_press == "h":
                key_press = False
                self.menu()
            elif key_press == "q":
                return
            else:
                print("Please try again. That wasn't a valid input.")
                key_press = input()
                
    def text_message(self):
        wants_continue = True
        while wants_continue:
            print("\n Please enter a phone number below as one string of numbers like this: 1234567890")
            phone_num = input()
            if return_to_menu(phone_num):
                wants_continue = False
                self.menu()
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
                self.menu()
        
        self.phone_num = phone_num
        new_cond = True
        
        while new_cond: 
            print("\nPlease type your message and press enter when finished.")
            message = input()
            print("\nPress 1 to send. Press 2 to edit. Press 3 to translate. Press h for more options.")
            key_num = input()
            if key_num == "1":
                new_cond = False
                self.phone_num = "+1" + self.phone_num
                receive = "+14159919818"
                self.message = message
                try:
                    messaging(self.message)  # body, to = "+14159919818", from_ = phone_number
                    print("Message sent. Thank you")
                    new_cond = False
                    self.menu()
                except Exception as e:
                    print("An error has occured: " + e)
                    print("/n Please try again")
                    new_cond = False
                    self.menu()
            elif key_num == "2":
                continue
            elif key_num == "3":
                self.comm_translate(self.message, "German")
                print("\nPress 1 to send. Press 2 to edit. Press h for more options.")
                key_num = input()
                if key_num == "1":
                    new_cond = False
                    try:
                        messaging(self.message)  # body, to = "+14159919818", from_ = phone_number
                        print("Message sent. Thank you")
                        new_cond = False
                        self.menu()
                    except Exception as e:
                        print("An error has occured: " + e)
                        print("/n Please try again")
                        new_cond = False
                        self.menu()
                elif key_num == "2":
                    continue
                elif return_to_menu(key_num):
                    new_cond = False
                    self.menu()
                else:
                    continue
            elif return_to_menu(key_num):
                new_cond = False
                self.menu()
            else:
                continue 

    def email(self):
        return
    
    def comm_translate(self, text, lang):

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5545")

        socket.send_json({'lang': lang, 'text': text})
        time.sleep(.5)
        message = socket.recv_json
        socket.close()
        return message

    def sign_up(self):
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
                self.menu()
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
                self.menu()
            self.sign_up_backend(new_user, four)
            print("You are now logged in as: " + new_user)
            self.user_name = new_user
            self.pin = four
            cond = False
        self.signed_menu()
        return

    def login(self):
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
                self.menu()
            while new_cond:
                print("Please enter your pin number of four digits.")
                pin = input()
                if return_to_menu(pin):
                    cond, new_cond = False, False
                    self.menu()
                if check_four(pin) is False:
                    count +1
                    print("That pin was either incorrect.\n")
                    if count == 3:
                        print("You have entered your pin too many times. Return to the main menu.")
                        cond, new_cond = False, False
                        self.menu()
                    continue
                if self.login_check(user, pin) is False:
                    count +1
                    print("That pin was incorrect")
                    if count == 3:
                        print("You have entered your pin too many times. Return to the main menu.")
                        cond, new_cond = False, False
                        self.menu()
                    continue
                
                cond, new_cond = False, False
                self.login_backend(user, pin)
            self.menu()

    def more_options():
        print("There are no more options.")
        menu()
        return

    def signed_menu(self):
        return

    def sign_up_backend(self, new_user, pin):
        return True

    def login_backend(self, user, pin):
        return

    def login_check(self, user, pin):
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






