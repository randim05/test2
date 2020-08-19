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
    if len(l) == 2 and all_isalpha(l[0]) and l[1].isdigit():
        return l
    else:
        return False

valid_var = {}

while True:
    try:
        user_input = input()
        if "=" in user_input:
            c = valid_assignment(user_input)
            if c:
                valid_var[c[0]] = c[1]
            else:
                print("Invalid identifier")
        elif user_input.startswith('/'):
            if user_input == "/exit":
                print("Bye!")
                break
            elif user_input == "/help":
                print("The program calculates the sum of numbers")
                continue
    except:
        pass