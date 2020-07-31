# Write your code here
import random

f = open('rating.txt', 'r')
print('Enter your name: ', end='')
name_input = input()
print('Hello, ' + name_input)

dict_name_rating = {}
for i in f.readlines():
    i.strip()
    name, rating = i.split(' ')
    rating = int(rating)
    # print(name, rating)
    dict_name_rating[name] = rating
if name_input not in dict_name_rating:
    dict_name_rating[name_input] = 0
f.close()
f = open('rating.txt', 'w')

u_i = input()
while u_i != "!exit":
    # u_i = input()
    if u_i == "!rating":
        print("Your rating: " + str(dict_name_rating[name_input]))
        # u_i = input()
    ans = ['rock', 'paper', 'scissors']
    if u_i in ans:
        pc_a = random.choice(ans)
        if u_i == pc_a:
            print("There is a draw (%s)" % u_i)
            dict_name_rating[name_input] += 50
        elif u_i != pc_a:
            if u_i == 'rock' and pc_a == "scissors":
                print("Well done. Computer chose % s and failed" % pc_a)
                dict_name_rating[name_input] += 100
            elif u_i == 'rock' and pc_a == "paper":
                print("Sorry, but computer chose %s" % pc_a)
            elif u_i == 'scissors' and pc_a == "paper":
                print("Well done. Computer chose % s and failed" % pc_a)
                dict_name_rating[name_input] += 100
            elif u_i == 'scissors' and pc_a == "rock":
                print("Sorry, but computer chose %s" % pc_a)
            elif u_i == 'paper' and pc_a == "rock":
                print("Well done. Computer chose % s and failed" % pc_a)
                dict_name_rating[name_input] += 100
            elif u_i == 'paper' and pc_a == "scissors":
                print("Sorry, but computer chose %s" % pc_a)
        u_i = input()
        # continue
    elif u_i == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
        u_i = input()
# dict_name_rating[name_input] = rating
for i in dict_name_rating:
    print(i, dict_name_rating[i], file=f)
f.close()