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
milk_for_cappuccino = 10
cof_for_cappuccino = 12
cappuccino_costs = 6


def buy(action):
    if int(action) == 3:
        global water, milk, cof, d_cups, money
        water -= water_for_espresso
        milk -= milk_for_espresso
        cof -= cof_for_espresso
        d_cups -= 1
        money += espresso_costs

    if int(action) == 2:
        global water, milk, cof, d_cups, money
        water -= water_for_latte
        milk -= milk_for_latte
        cof -= cof_for_latte
        d_cups -= 1
        money += latte_costs

    if int(action) == 3:
        global water, milk, cof, d_cups, money
        water = water - water_for_cappuccino
        milk = milk - milk_for_cappuccino
        cof -= cof_for_cappuccino
        d_cups -= 1
        money += cappuccino_costs
    take()

def fill():
    print("Write how many ml of water do you want to add:")
    global water
    water = int(input("> "))
    print("Write how many ml of milk do you want to add:")
    global milk
    milk = int(input("> "))
    print("Write how many grams of coffee beans do you want to add:")
    global cof
    cof = int(input("> "))
    print("Write how many disposable cups of coffee do you want to add:")
    global d_cups
    d_cups = int(input("> "))
    take()


def take():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(cof) + " of coffee beans")
    print(str(d_cups) + " of disposable cups")
    print(str(money) + " of money")


print("Write action (buy, fill, take):")
action = input("> ")
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take(action)


# w = water // water_for_cup
# m = milk // milk_for_cup
# c = cof // cof_for_cup
#
# if (min(w, m, c)) < cups:
#     print("No, I can make only {0} cups of coffee".format(str(min(w, m, c))))
# elif (min(w, m, c)) == cups:
#     print("Yes, I can make that amount of coffee")
# else:
#     print("Yes, I can make that amount of coffee (and even " +
#             str(min(w, m, c) // cups - 1) +  # min res determine how mach
#             " more than that)")