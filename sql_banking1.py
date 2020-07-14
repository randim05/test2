# Write your code here
import random
import sqlite3
conn = sqlite3.connect('card.s3db')  # cards saves here) card_number : CreditCard
cur = conn.cursor()
cur.execute("DROP TABLE card")
conn.commit()
cur.execute('''CREATE TABLE card (
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0)''')
conn.commit()

class CreditCard:
    def __init__(self):
        x = True
        while x:
            temp_card_number = "400000" + "%.10d" % random.randint(0, 9999999999)
            # if not cur.execute('select * from card where number = %s'
            #                    % temp_card_number):
            self.card_number = self.luhn(temp_card_number)
            self.pin = "%0.4d" % random.randint(0, 9999)  # type str!
            self.balace = 0
            print("Your card has been created")
            print("Your card number:")
            print(self.card_number)
            print("Your card PIN:")
            print(self.pin)
            cur.execute("INSERT INTO card VALUES (%d, %s, %s, %d)"
                        % (int(temp_card_number), self.card_number,
                           self.pin, self.balace))
            conn.commit()
            x = False



    def luhn(self, x):
        x = [int(i) for i in x]
        even = [i * 2 for i in x[-2::-2]]
        even = [i - 9 if i > 9 else i for i in even]
        odd = [i for i in x[-3::-2]]
        s = sum(even) + sum(odd)
        if s % 10 == 0:
            x = ''.join(map(str, x))
            return x
        else:
            x[-1] = 10 - s % 10
            x = ''.join(map(str, x))
            return x



do_some = '1'
while do_some != 'exit':
    print('1. Create an account')
    print("2. Log into account")
    print("0. Exit")

    user_input = input()
    if user_input == "1":
        temp_card = CreditCard()  # __init__
        # cards[temp_card.card_number] = temp_card
    elif user_input == "2":
        print("Enter your card number:")
        login_card = input()
        print("Enter your PIN:")
        login_pin = input()
        if cur.execute('select * from card where number = %s' % login_card):
            # ctl = cur.execute('select * from card where number = %s'
            #                   % login_card)
            if cur.execute('select * from card where pin = %s' % login_pin):
                print("You have successfully logged in!")
                print()
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                u_i = input()
                if u_i == "1":
                    print("Balance: " +
                        cur.execute('select balance from card where number = %s'
                                    % login_card))
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