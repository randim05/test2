import random
u_i = input()
while u_i != "!exit":
    ans = ['rock', 'paper', 'scissors']
    if u_i in ans:
        pc_a = random.choice(ans)
        if u_i == pc_a:
            print("There is a draw (%s)" % u_i)
        elif u_i != pc_a:
            if u_i == 'rock' and pc_a == "scissors":
                print("Well done. Computer chose % s and failed" % pc_a)
            elif u_i == 'rock' and pc_a == "paper":
                print("Sorry, but computer chose %s" % pc_a)
            elif u_i == 'scissors' and pc_a == "paper":
                print("Well done. Computer chose % s and failed" % pc_a)
            elif u_i == 'scissors' and pc_a == "rock":
                print("Sorry, but computer chose %s" % pc_a)
            elif u_i == 'paper' and pc_a == "rock":
                print("Well done. Computer chose % s and failed" % pc_a)
            elif u_i == 'paper' and pc_a == "scissors":
                print("Sorry, but computer chose %s" % pc_a)
        u_i = input()
        # continue
    else:
        print("Invalid input")
        u_i = input()
print("Bye!")