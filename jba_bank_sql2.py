# Write your code here
import random
import sqlite3


conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
# cur.execute("CREATE DATABASE card")
# conn.commit()
# cur.execute("DROP TABLE card")
# conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0)''')
conn.commit()


class CreditCard:
    def __init__(self):
        x = True
        while x:
            temp_card_number = "400000" + "%.10d" % random.randint(0,
                                                                   9999999999)
            # if temp_card_number in cur.execute('select number from card where number = %s' % temp_card_number).fetchall():  #.fetchone()[0] == temp_card_number:
            #     continue
            # else:
            self.number = self.luhn(temp_card_number)
            self.pin = "%0.4d" % random.randint(0, 9999)  # type str!
            self.balace = 0
            print("Your card has been created")
            print("Your card number:")
            print(self.number)
            print("Your card PIN:")
            print(self.pin)
            cur.execute("INSERT INTO card (number, pin, balance) VALUES (?, ?, ?)",(self.number, self.pin, self.balace))
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
            x[-1] = 10 - (s % 10 - x[-1])
            x = ''.join(map(str, x))
            return x


def luhn_test(x):
    x = [int(i) for i in x]
    even = [i * 2 for i in x[-2::-2]]
    even = [i - 9 if i > 9 else i for i in even]
    odd = [i for i in x[-3::-2]]
    s = sum(even) + sum(odd) + x[-1]
    return s % 10 == 0


do_some = '1'
while do_some != 'Exit':
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
        cur.execute('select number from card where number = ?',login_card)
        num_card = cur.fetchone()
        if num_card:
            # ctl = cur.execute('select * from card where number = %s'
            #                   % login_card)
            cur.execute('select number from card where pin = ?',login_pin)
            num_card_pin = cur.fetchone()
            if num_card == num_card_pin:
                print("You have successfully logged in!")
                print()
                inner_chek = 1
                while inner_chek != "Exit":
                    if num_card == num_card_pin:
                        # print("You have successfully logged in!")
                        # print()
                        print("1. Balance")
                        print("2. Add income")
                        print("3. Do transfer")
                        print("4. Close account")
                        print("5. Log out")
                        print("0. Exit")
                        u_i = input()
                        if u_i == "1":
                            print("Balance: " + str(
                                cur.execute('select balance from card where number = ?',login_card).fetchone()[0]))
                            # continue
                        elif u_i == "2":
                            print("Enter income:")
                            c = int(input())
                            bal1 = cur.execute('select balance from card where number = ?',login_card)
                            bal = bal1.fetchone()[0] + c
                            # print(bal1.fetchone()[0])
                            cur.execute('UPDATE card  SET balance = ? WHERE number = ?',(bal, login_card))
                            conn.commit()
                            print("Income was added!")

                        elif u_i == "3":
                            print("Transfer")
                            print("Enter card number:")
                            cn = input()
                            if luhn_test(cn):
                                if cn == login_card:
                                    print("You can't transfer money to the same account!")
                                h = cur.execute("select * from card where number = ?",cn).fetchone()[0]   # !!!!!!!!!!!
                                if h:
                                    print("Enter how much money you want to transfer:")
                                    trans = int(input())
                                    bal1 = cur.execute('select balance from card where number = ?',cn).fetchone()[0]
                                    if bal1 >= trans:
                                        x = int(bal1) - trans
                                        cur.execute("UPDATE card SET balance = ? WHERE number = ?",(str(x), cn))
                                        conn.commit()
                                        print("Success!")
                                        continue
                                    else:
                                        print("Not enough money!")
                                        continue
                                else:
                                    print("Such a card does not exist.")
                            else:
                                print("Probably you made mistake in the card number. Please try again!")
                            # pass
                        elif u_i == "4":
                            cur.execute("DELETE FROM card WHERE number = ?",login_card)
                            conn.commit()
                            print("The account has been closed!")
                            inner_chek = "Exit"
                        elif u_i == "5":
                            print("You have successfully logged out!")
                            inner_chek = "Exit"
                        elif u_i == "0":
                            print("Bye!")
                            inner_chek = "Exit"
                            do_some = "Exit"
                            conn.commit()
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")
    elif user_input == "0":
        print("Bye!")
        do_some = "Exit"
        conn.commit()
# conn.commit()
conn.close()
