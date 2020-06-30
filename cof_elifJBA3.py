# Write your code here
# input
print("Write how many ml of water the coffee machine has:")
water = int(input("> "))
print("Write how many ml of milk the coffee machine has:")
milk = int(input("> "))
print("Write how many grams of coffee beans the coffee machine has:")
cof = int(input("> "))
print("Write how many cups of coffee you will need:")
cups = int(input("> "))

# const
water_for_cup = 200
milk_for_cup = 50
cof_for_cup = 15
w = water // water_for_cup
m = milk // milk_for_cup
c = cof // cof_for_cup
# print("from has water i can do " + str(water // water_for_cup) + " cups")
# print("from has milk i can do " + str(milk // milk_for_cup) + " cups")
# print("from has coffe i can do " + str(cof // cof_for_cup) + " cups")
# print(min(w, m, c))
if (min(w, m, c)) < cups:
    print("No, I can make only {0} cups of coffee".format(str(min(w, m, c))))
elif (min(w, m, c)) == cups:
    print("Yes, I can make that amount of coffee")
else:
    print("Yes, I can make that amount of coffee (and even " +
            str(min(w, m, c) // cups - 1) +  # min res determine how mach
            " more than that)")

# # find intermediate
# w = water // water_for_cup
# m = milk // milk_for_cup
# c = cof // cof_for_cup
# print((w or m or c) // cups - 2)
# print(w, m, c)


# if w and m and c:                   # can do some 1 cup
#     # if w == cups or m == cups or c == cups:  # can do only 1 cup
#     #     print("Yes, I can make that amount of coffee")
#     if w > cups or m > cups or c > cups:                           # can do more
#         print(
#             "Yes, I can make that amount of coffee (and even " +
#             str((w or m or c) // cups - 1) +  # min res determine how mach
#             " more than that)"
#         )
# # if (cups * water_for_cup >= water and
# #         cups * milk_for_cup >= milk and
# #         cups * cof_for_cup >= cof):
# #     # if all res fully
# #     # if there are as many resources as you need
# #     if (cups * water_for_cup == water or
# #             cups * milk_for_cup == milk or
# #             cups * cof_for_cup == cof):
# #         print("Yes, I can make that amount of coffee")
# #
# #     elif cups * water_for_cup > water:
# #         print("Yes, I can make that amount of coffee (and even "
# #               + str(water // (cups * water_for_cup) - 1)
# #               + " more than that)")
# #     elif cups * milk_for_cup > milk:
# #         print("Yes, I can make that amount of coffee (and even "
# #               + str(milk // (cups * milk_for_cup) - 1)
# #               + " more than that)")
# #     elif cups * cof_for_cup > cof:
# #         print("Yes, I can make that amount of coffee (and even "
# #               + str(cof // (cups * cof_for_cup) - 1)
# #               + " more than that)")
#
# else:
#     print(
#         "No, I can make only {0} cups of coffee".format(str((w or m or c)))
#     )
