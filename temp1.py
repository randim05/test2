#
# temp_card_number = '400000088324782'
# x = 3
# temp_card_number = temp_card_number + str(x)
# print(temp_card_number)

# import random
# temp_card_number = "400000" + "%.9d" % random.randint(0, 999999999)
# res = 0
# even = [int(i) * 2 for i in temp_card_number[::2]]
# odd = sum([int(i) for i in temp_card_number[1::2]])
# for i in even:
#     if i > 9:
#         i -= 9
# even = sum(even)
# res = even + odd
# if res % 10 == 0:
#     x = 0
# else:
#     x = 10 - res % 10
# temp_card_number = temp_card_number + str(x)
# print(temp_card_number)

# Write your code here
import random
cards = {}  # cards saves here) card_number : CreditCard


class CreditCard:
    def __init__(self):
        temp_card_number = "400000" + "%.10d" % random.randint(0, 9999999999)
        while not self.luhn(temp_card_number):
            temp_card_number = "400000" + "%.10d" % random.randint(0, 9999999999)
            if temp_card_number not in cards:
                self.card_number = temp_card_number
                self.pin = "%0.4d" % random.randint(0, 9999)  # type str!
                self.balace = 0
                print("Your card has been created")
                print("Your card number:")
                print(self.card_number)
                print("Your card PIN:")
                print(self.pin)
            else:
                continue

        # pass

    def luhn(self, x):
        res = 0
        even = [int(i) * 2 for i in x[-1::-2]]
        odd = sum([int(i) for i in x[-2::-2]])
        for i in even:
            if i > 9:
                i -= 9
        even = sum(even)
        res = even + odd
        if res % 10 == 0:
            return True
        else:
            return False



do_some = '1'
while do_some != 'exit':
    print('1. Create an account')
    print("2. Log into account")
    print("0. Exit")

    user_input = input()
    if user_input == "1":
        temp_card = CreditCard()  # __init__
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
                    continue
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


