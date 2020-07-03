# import random
# print(type("%0.4d" % random.randint(0, 9999)))

# Write your code here
import random
cards = {}  # cards saves here) card_number : CreditCard


class CreditCard:
    def __init__(self):
        temp_card_number = "400000" + "%.10d" % random.randint(0, 9999999999)  # str!
        if temp_card_number in cards:
            temp_card_number = "400000" + "%.10d" % random.randint(0, 9999999999)
        self.card_number = temp_card_number
        self.pin = "%0.4d" % random.randint(0, 9999)  # type str!
        self.balace = 0
        print("Your card has been created")
        print("Your card number:")
        print(self.card_number)
        print("Your card PIN:")
        print(self.pin)
        # pass


do_some = '1'
while do_some != 'exit':
    print('1. Create an account')
    print("2. Log into account")
    print("0. Exit")

    user_input = input()
    if user_input == "1":
        temp_card = CreditCard() # __init__
        cards[temp_card.card_number] = temp_card
    elif user_input == "2":
        print("Enter your card number:")
        login_card = input()
        print("Enter your PIN:")
        login_pin = input()
        if login_card in cards:
            ctl = cards[login_card]  # class CreditCard
            if ctl.pin == login_pin:
                print("You have successfully logged in!")
                print()
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                u_i = input()
                if u_i == "1":
                    print("Balance: " + str(ctl.balace))
                elif u_i == "2":
                    print("You have successfully logged out!")
                elif u_i == "0":
                    print("Bye!")
                    do_some = "exit"
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")
    elif user_input == "0":
        print("Bye!")
        do_some = "exit"


