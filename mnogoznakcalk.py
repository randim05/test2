# write your code here
def n(znak, digit):
    if "-" in znak:
        if len(znak) % 2 == 0:
            return int(digit)
        else:
            return int(digit) * -1
    return digit

while True:
    z = input()
    if z == "/exit":
        print("Bye!")
        break
    elif z == "/help":
        print("The program calculates the sum of numbers")
        continue
    elif z == '':
        continue
    else:
        y = z.split()
        print(y)
        # print(sum([n(i, j) for i, j in y]))
        continue