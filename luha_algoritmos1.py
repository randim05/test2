# number = '4000009762111818'
# print(len(number))
# tmp = [int(i) * 2 for i in list(number)][:-1]
# print(len(tmp))
# res = 0
# print(tmp)
# tmp = [i if i <= 9 else i - 9 for i in tmp]
# print(tmp)
# res = sum(tmp)
# print(res)
# numberq = number[:-1] + str(10 - (res % 10))
# print(tmp)
# print(number)
# print(numberq)
# print(len(numberq))

# import random
# # cards = {}
# temp_card_number = "400000" + "%.9d" % random.randint(0, 999999999)  # str!
# print(temp_card_number)
# print(len(temp_card_number))
# # if temp_card_number in cards:
# #     temp_card_number = "400000" + "%.9d" % random.randint(0, 999999999) #15
# luha = [int(i) * 2 for i in temp_card_number][:-1]
# luha = [i if i <= 9 else i - 9 for i in luha]
# temp_card_number = temp_card_number + str(10 - (sum(luha) % 10))
# print(temp_card_number)
# print(len(temp_card_number))

