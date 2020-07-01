water = 400
milk = 540
cof = 120
d_cups = 9
money = 550

espresso = 1
water_e = 250
milk_e = 0
cof_e = 16
money_e = 4

latte = 2
water_l = 350
milk_l = 75
cof_l = 20
money_l = 7

cappuccino = 3
water_c = 200
milk_c = 100
cof_c = 12
money_c = 6


def buy(x):  # продать
    global water, milk, cof, d_cups, money
    x = int(x)
    if x == 1:
        if water < water_e:
            print("Sorry, not enough water!")
        elif milk < milk_e:
            print("Sorry, not enough milk!")
        elif cof < cof_e:
            print("Sorry, not enough coffee beans!")
        elif d_cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= water_e
            milk -= milk_e
            cof -= cof_e
            d_cups -= 1
            money += money_e
    elif x == 2:
        if water < water_l:
            print("Sorry, not enough water!")
        elif milk < milk_l:
            print("Sorry, not enough milk!")
        elif cof < cof_l:
            print("Sorry, not enough coffee beans!")
        elif d_cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= water_l
            milk -= milk_l
            cof -= cof_l
            d_cups -= 1
            money += money_l
    elif x == 3:
        if water < water_c:
            print("Sorry, not enough water!")
        elif milk < milk_c:
            print("Sorry, not enough milk!")
        elif cof < cof_c:
            print("Sorry, not enough coffee beans!")
        elif d_cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            print()
            water -= water_c
            milk -= milk_c
            cof -= cof_c
            d_cups -= 1
            money += money_c

    # take()


def fill():   # напонить
    global water, milk, cof, d_cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    cof += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    d_cups += int(input())


def take():  # отдать все деньги
    global money
    print("I gave you $" + str(money))
    money = 0


# def work():
action = "c"


def remaining():  # состояние
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(cof) + " of coffee beans")
    print(str(d_cups) + " of disposable cups")
    print(str(money) + " of money")
    print()


while action != "exit":
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino"
              ", back - to main menu:")
        d = input()
        if d == 'back':
            continue
        else:
            buy(d)
    elif action == "remaining":
        remaining()
    elif action == "fill":
        fill()
    elif action == "take":
        take()


