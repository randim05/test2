# write your code here
def all_isalpha(x):
    for i in x:
        try:
            int(i)
            return False
        except ValueError:
            continue
    return True

def valid_assignment(x):
    l = [i.strip() for i in x.split("=")]
    if len(l) == 2:
        if all_isalpha(l[0]):
            if l[1].isdigit():
                valid_var[hash(l[0])] = l[1]
                return l
            elif l[1].isalpha() and all_isalpha(l[1]):
                if hash(l[1]) in valid_var:
                    valid_var[hash(l[0])] = valid_var[hash(l[1])]
                    return [l[0], valid_var[hash(l[0])]]
                else:
                    print("Invalid identifier")
                    return False
            else:
                print("Invalid identifier")
                return False
        else:
            print("Invalid identifier")
            return False
    else:
        print('Invalid assignment')
        return False

def calc(args):
    # for i in args:
    #     i = i.strip()
    # res = int(args[0])
    # for i in range(len(args)):
    #     if args[i] == "+":
    #         # a = i.index()
    #         res += int(args[i+1])
    #     elif args[i] == "-":
    #         # a = i.index()
    #         res -= int(args[i+1])
    # return res
    print(eval(''.join(args)))


valid_var = {}

while True:
#     try:
        user_input = input()
        if "=" in user_input:
            valid_assignment(user_input)
        elif user_input.startswith('/'):
            if user_input == "/exit":
                print("Bye!")
                break
            elif user_input == "/help":
                print("The program calculates the sum of numbers")
                continue
            else:
                print("Unknown command")
        elif "+" in user_input or "-" in user_input:
            if " " in user_input:
                list_user_oper = user_input.split(' ')
                list_user_oper = [i.strip() for i in list_user_oper]
                # print(exec(''.join(list_user_oper)))
            out_list = []
            for i in list_user_oper:
                if hash(i) in valid_var:
                    out_list.append(valid_var[hash(i)])
                else:
                    out_list.append(i)
            calc(out_list)
        elif hash(user_input.strip()) in valid_var:
            print(valid_var[hash(user_input)])

        elif user_input == '':
            continue
        elif hash(user_input.strip()) not in valid_var:
            print("Unknown variable")
        else:
            print('Invalid assignment')