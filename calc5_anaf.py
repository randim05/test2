
variable_storage = {}


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
    digits = []
    alphas = []
    math_zn = []
    res = []
    half_moon = []
    for i in ui:
        if i.isdigit():  # if coming digit
            if len(alphas) != 0 or len(math_zn) == 0:  # was alphas and not math_zn
                return "Invalid variables"  # digit after symbol not valid variable
            else:
                res.append(''.join(alphas))  # coming digit after symbol
                alphas = []  # drop symbol
                res.append(''.join(math_zn))  # and after math_zn
                math_zn = []  # drop math_zn
            digits.append(i)  # and go create next digit

        elif i.isalpha():  # if coming alphas
            if len(digits) != 0 or len(math_zn) == 0:  # a was digits or no math_zn
                return "Invalid expression"  #
            else:
                res.append(''.join(digits))  # coming digit after symbol
                digits = []  # drop symbol
                res.append(''.join(math_zn))  # and after math_zn
                math_zn = []
            alphas.append(i)
        elif i in (' ', '\n', "\t"):
            continue

        elif i in ("+", "-", "/", "*"):
            math_zn.append(i)
        elif i == ')' and len(half_moon) == 0:
            return "Invalid expression"
        elif i == "(":
            half_moon.append(i)
        elif ui.starstwhith(")"):
            return "Invalid expression"


def create_postfix_notation(ui):
    pass


def calc_postfix(ui_in_postfix):
    pass


exit_flag = 1
# main loop
while exit_flag:
    user_input = input()  # user input string
    if "=" in user_input:
        if ansigment_validator(user_input):
            pass
        else:
            continue
