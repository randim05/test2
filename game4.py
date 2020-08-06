import random
rating_dict = {}
f = open("rating.txt", 'r')
for i in f.readlines():
    i.strip()
    y = i.split()
    rating_dict[y[0]] = int(y[1])
f.close()

print('Enter your name: ', end='')
user_name_input = input()           # имя пользователя
print('Hello, ' + user_name_input)

if user_name_input not in rating_dict:  # добавляем пользователя если новый
    rating_dict[user_name_input] = 0

term = input()                # ввод набора для игры
if term == '':                # если ввод пустой то используем стандартный
    term_list = ['rock', 'paper', 'scissors']
else:                         # иначе пользовательский
    term_list = [term.split(',')]

print('Okay, let\'s start')


def def_game(u_i_dgf, pc_a_dgf):
    if u_i_dgf == 'rock' and pc_a_dgf == "scissors":
        print("Well done. Computer chose % s and failed" % pc_a_dgf)
        rating_dict[user_name_input] += 100
    elif u_i_dgf == 'rock' and pc_a_dgf == "paper":
        print("Sorry, but computer chose %s" % pc_a_dgf)

    elif u_i_dgf == 'scissors' and pc_a_dgf == "paper":
        print("Well done. Computer chose % s and failed" % pc_a_dgf)
        rating_dict[user_name_input] += 100
    elif u_i_dgf == 'scissors' and pc_a_dgf == "rock":
        print("Sorry, but computer chose %s" % pc_a_dgf)

    elif u_i_dgf == 'paper' and pc_a_dgf == "rock":
        print("Well done. Computer chose % s and failed" % pc_a_dgf)
        rating_dict[user_name_input] += 100
    elif u_i_dgf == 'paper' and pc_a_dgf == "scissors":
        print("Sorry, but computer chose %s" % pc_a_dgf)


def game(u_i_dgf, pc_a_dgf, term_list_dgf):
    ttl = term_list_dgf[:]                  # temp term list
    med = len(ttl) // 2
    # польз ввел знач в середине список не надо менять
    if ttl.index(u_i_dgf) == med:
        if ttl.index(u_i_dgf) > ttl.index(pc_a_dgf):
            print("Well done. Computer chose % s and failed" % pc_a_dgf)
            rating_dict[user_name_input] += 100
        elif ttl.index(u_i_dgf) < ttl.index(pc_a_dgf):
            print("Sorry, but computer chose %s" % pc_a_dgf)

    # пользователь ввел значение правее середины
    elif ttl.index(u_i_dgf) > med:
        x = ttl.index(u_i_dgf) - med  # влево от полз ввода на пол длины
        ttl2 = ttl[x:] + ttl[:x]
        # u_i=6 123x456y7 -> 3456712
        if ttl2.index(u_i_dgf) > ttl2.index(pc_a_dgf):
            print("Well done. Computer chose % s and failed" % pc_a_dgf)
            rating_dict[user_name_input] += 100
        elif ttl2.index(u_i_dgf) < ttl2.index(pc_a_dgf):
            print("Sorry, but computer chose %s" % pc_a_dgf)

    # пользователь ввел значение левее середины
    elif ttl.index(u_i_dgf) < med:
        x = ttl.index(u_i_dgf) + med  # влево от полз ввода на пол длины
        ttl2 = ttl[x+2:] + ttl[:x+2]
        # u_i=2 i=1 m=3 [5:]+[:5] 1234567 -> 6712345
        if ttl2.index(u_i_dgf) > ttl2.index(pc_a_dgf):
            print("Well done. Computer chose % s and failed" % pc_a_dgf)
            rating_dict[user_name_input] += 100
        elif ttl2.index(u_i_dgf) < ttl2.index(pc_a_dgf):
            print("Sorry, but computer chose %s" % pc_a_dgf)


while True:
    u_i = input()                    # выбор пользователя
    pc_a = random.choice(term_list)  # выбор пк
    if u_i == "!rating":
        print("Your rating: " + str(rating_dict[user_name_input]))
        continue
    elif u_i == "!exit":
        print("Bye!")
        break
    elif u_i == pc_a:
        print("There is a draw (%s)" % u_i)
        rating_dict[user_name_input] += 50
        continue
    elif u_i in term_list:
        if term_list == ['rock', 'paper', 'scissors']:
            def_game(u_i, pc_a)
            continue
        else:
            game(u_i, pc_a, term_list)
            continue
    else:
        print("Invalid input")
        continue



f = open('rating.txt', 'w')  # пишем словарь рейтинга в файл
for i in rating_dict:
    print(i, rating_dict[i], file=f)
f.close()
