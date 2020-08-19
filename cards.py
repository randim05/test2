cards = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
         "Jack":11, "Queen":12, "King":13, "Ace":14}
sum = 0
ch = 1
u_i = []
while len(u_i) < 6:
    u_i.append(input())
# u_i = input().split('/n')
for i in u_i:
    i.strip()
    if i in cards:
        sum += cards[i]
        # ch += 1

print(sum/len(u_i))