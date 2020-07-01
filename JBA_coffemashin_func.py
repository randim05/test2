# Write your code here
# input
# print("Write how many ml of water the coffee machine has:")
# water = int(input("> "))
# print("Write how many ml of milk the coffee machine has:")
# milk = int(input("> "))
# print("Write how many grams of coffee beans the coffee machine has:")
# cof = int(input("> "))
# print("Write how many cups of coffee you will need:")
# cups = int(input("> "))

water = 400
milk = 540
cof = 120
d_cups = 9
money = 550

espresso = 1
water_for_espresso = 250
milk_for_espresso = 0
cof_for_espresso = 16
espresso_costs = 4

latte = 2
water_for_latte = 350
milk_for_latte = 75
cof_for_latte = 20
latte_costs = 7

cappuccino = 3
water_for_cappuccino = 200
milk_for_cappuccino = 100
cof_for_cappuccino = 12
cappuccino_costs = 6


def out_has():
    print()
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(cof) + " of coffee beans")
    print(str(d_cups) + " of disposable cups")
    print(str(money) + " of money")


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    x = int(input())
    global water
    global milk
    global cof
    global d_cups
    global money
    out_has()
    if x == 1:
        water = water - water_for_espresso
        milk = milk - milk_for_espresso
        cof = cof - cof_for_espresso
        d_cups = d_cups - 1
        money = money + espresso_costs

    if x == 2:
        water = water - water_for_latte
        milk = milk - milk_for_latte
        cof = cof - cof_for_latte
        d_cups = d_cups - 1
        money = money + latte_costs

    if x == 3:
        water = water - water_for_cappuccino
        milk = milk - milk_for_cappuccino
        cof = cof - cof_for_cappuccino
        d_cups = d_cups - 1
        money = money + cappuccino_costs
    out_has()


def fill():
    global water
    global milk
    global cof
    global d_cups
    out_has()
    print("Write how many ml of water do you want to add:")
    water = water + int(input())
    print("Write how many ml of milk do you want to add:")
    milk = milk + int(input())
    print("Write how many grams of coffee beans do you want to add:")
    cof = cof + int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    d_cups = d_cups + int(input())
    out_has()


def take():
    global money
    out_has()
    print("I gave you $" + str(money))
    money = 0
    out_has()


print("Write action (buy, fill, take):")
action = input()
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
