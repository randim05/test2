import random


def def_game():
    u_i = input()
    pc_a = random.choice(term_list)
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
    if u_i == "!exit":
        print("Bye!")
        return 0
    #     break
    # u_i = input()


def game():
    u_i = input()
    pc_a = random.choice(term_list)  # выбираем вариант пк
    user_index = term_list.index(u_i)  # индекс ввода польз
    pc_index = term_list.index(pc_a)  # инд выбор а пк
    new_list_for_compare = term_list[user_index + 1:] + term_list[
                                                        :user_index]
    # создаем новый список
    #  то что после польз ввода в начало и с начала до польз ввода далее
    mediana = len(new_list_for_compare) / 2  # середина нов листа

    if u_i == pc_a:  # ничья если ввели одинаковое
        print("There is a draw (%s)" % u_i)
        dict_name_rating[name_input] += 50

    elif u_i != pc_a:
        if pc_index < mediana:
            print("Well done. Computer chose % s and failed" % pc_a)
            dict_name_rating[name_input] += 100
        elif pc_index >= mediana:
            print("Sorry, but computer chose %s" % pc_a)
    # u_i = input()
    # continue

    elif u_i == "!exit":
        print("Bye!")
        return 0


f = open('rating.txt', 'r')  # открываем на чтение
print('Enter your name: ', end='')
name_input = input()  # имя пользователя
print('Hello, ' + name_input)

dict_name_rating = {}
for i in f.readlines():          # построчно читаем
    i.strip()                    # обрезаем лишнее с краев
    name, rating = i.split(' ')  # разбиваем и присваиваем
    rating = int(rating)
    # print(name, rating)
    dict_name_rating[name] = rating     # пихаем в словарь
if name_input not in dict_name_rating:  # если нет введенного имени в файле
    dict_name_rating[name_input] = 0    # создаем в словаре с 0 рейтингом
f.close()                               # закрываем на чтение
f = open('rating.txt', 'w')             # открываем на запись старый затираем,
#                                        т.к. инфа в словаре

term = input()                   # ввод набора для игры
if term == '':                   # если ввод пустой то используем стандартный
    term_list = ['rock', 'paper', 'scissors']
    print('Okay, let\'s start')
    def_game()
else:
    term_list = term.split(',')  # если нет то разбиваем по ,
    print('Okay, let\'s start')
    game()


for i in dict_name_rating:
    print(i, dict_name_rating[i], file=f)
f.close()
# u_i = input()                    # ход пользователя



