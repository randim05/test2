
variable_storage = {}

ZNAKS = ("+", "-", "/", "*")
DIGITS = "1234567890"
# def block


def all_isalpha(x):  # --> bool
    for i in x:  # if in string only letters
        try:
            int(i)
            return False
        except ValueError:
            continue
    return True


def ansigment_validator(ui):  # --> bool
    ui_split_list = [i.strip() for i in ui.split("=")]
    if len(ui_split_list) == 2:
        if all_isalpha(ui_split_list[0]):
            try:
                int(ui_split_list[1])
                variable_storage[hash(ui_split_list[0])] = str(int(ui_split_list[1]))
                return True
            except ValueError:
                print('Invalid assignment')
                return False
        elif all_isalpha(ui_split_list[0]) and all_isalpha(ui_split_list[1]):
            if hash(ui_split_list[1]) in variable_storage:
                variable_storage[hash(ui_split_list[0])] = variable_storage[hash(ui_split_list[1])]
                return True
            else:
                print("Invalid identifier")
                return False
        # else:
        #     print("Invalid identifier")
        #     return False
    else:
        print('Invalid assignment')
        return False


# 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
# -3+erwe545634df-)(-3*2


def ui_preprocessor(ui):
    if ui.starstwhith(")") or ui.endswith("("):
        print("Invalid expression")
        return False

    elif ui[-1] in ZNAKS:           # if ui ends +-*/
        print("Invalid expression")
        return False

    # ( ahead ) else Invalid expression
    was_left_bracket = 1                    # there was no opening bracket
    counter_left_bracket = 0
    for i in ui:
        if i == "(":
            was_left_bracket = 0            # ( ahead )
            counter_left_bracket += 1
        if i == ")" and was_left_bracket:  # coming ) and there was no opening bracket
            print("Invalid expression")
            return False
        if i == ")":                        # drop pair brackets
            counter_left_bracket -= 1
        if counter_left_bracket <= 0:       # drop all pair brackets
            was_left_bracket = 1

    # temp lists
    while "**" in ui or \
          "++" in ui or \
          "--" in ui or \
          "+-" in ui or \
          "-+" in ui or \
          "\n" in ui or \
          "\t" in ui:
        ui = ui.replace("**", "*")
        ui = ui.replace(" ", "")
        # ui.replace("/", "//")
        ui = ui.replace("++", "+")
        ui = ui.replace("--", "+")
        ui = ui.replace("+-", "-")
        ui = ui.replace("-+", "-")
        ui = ui.replace("\n", "")
        ui = ui.replace("\t", "")

    digits = []
    letters = []
    math_symbols = []
    bracket = []
    result = []

    # main parser loop
    for i in ui:
        if i in DIGITS:  # if coming digit
            if len(letters) != 0:  # or len(math_symbols) == 0:      # was alphas and not math_zn
                return "Invalid variables"  # digit after symbol not valid variable)
            digits.append(i)  # and go create next digit
        elif i.isalpha():  # if coming alphas
            if len(digits) != 0:  # a was digits or no math_zn
                return "Invalid expression"
            elif len(math_symbols) != 0:
                result.append(''.join(math_symbols))
                math_symbols = []
            letters.append(i)
        elif i == ' ':
            continue
        elif i in ZNAKS:
            if len(digits) != 0:
                result.append(''.join(digits))
                digits = []
            elif len(letters) != 0:
                x = ''.join(letters)
                if x in variable_storage:
                    result.append(variable_storage[x])
                else:
                    return "Invalid variables"
                letters = []
            result.append(i)
        else:
            result.append(i)
    if len(math_symbols) != 0:
        result.append(''.join(math_symbols))
    if len(digits) != 0:
        result.append(''.join(digits))
    return result


def create_postfix_notation(ui):
    quere = []
    stack = []
    for i in ui:
        if i.isdigit():
            stack.append(i)
        elif i in ("+", "-") and stack[-1] not in ("(", "*", "/"):
            stack.append(i)
        elif i in ("*", "/") and stack[-1] in ("+", "-"):
            stack.append(i)
        elif i in ("+", "-") and stack[-1] in ("*", "/"):
            while stack[-1] not in ("(", "*", "/"):
                quere.append(stack.pop())
            stack.append(i)
        elif i == ")":
            while stack:
                quere.append(stack.pop())
    while stack:
        quere.append(stack.pop())
    return int(calc_postfix(quere))


def calc_postfix(ui_in_postfix):
    stack = []
    for i in ui_in_postfix:
        if i.isdigit():
            stack.append(i)
        elif i == '+':
            x = stack.pop()
            y = stack.pop()
            z = int(y) + int(x)
            stack.append(str(z))
        elif i == '-':
            x = stack.pop()
            y = stack.pop()
            z = int(y) - int(x)
            stack.append(str(z))
        elif i == '/':
            x = stack.pop()
            y = stack.pop()
            z = int(y) // int(x)
            stack.append(str(z))
        elif i == '*':
            x = stack.pop()
            y = stack.pop()
            z = int(y) * int(x)
            stack.append(str(z))
    return stack[-1]


exit_flag = 1
# main loop
while exit_flag:
    user_input = input()  # user input string
    if "=" in user_input:
        if ansigment_validator(user_input):
            pass
        else:
            continue
