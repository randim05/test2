variable_storage = {}


def all_isalpha(x):
    for i in x:
        try:
            int(i)
            return False
        except ValueError:
            continue
    return True


def ui_in_list(so):
    temp_ui = []
    ui_digit = []
    ui_znaki = []
    ui_var = []
    for i in so:
        if i.isdigit():
            if len(ui_znaki) != 0:
                ui_digit.append(''.join(ui_znaki))
                ui_znaki = []
            temp_ui.append(i)
        elif i in ("+", "-", "/", "*"):
            if len(ui_var) != 0:
                temp_var_in_storage = ''.join(ui_var)
                if temp_var_in_storage in variable_storage:
                    ui_digit.append(variable_storage[temp_var_in_storage])
                else:
                    print("Unknow variable")
            ui_digit.append(''.join(temp_ui))
            temp_ui = []
            ui_znaki.append(i)
        elif i.isalpha():
            ui_var.append(i)

    ui_digit.append(''.join(temp_ui))
    return ui_digit


def create_postfix(so):
    temp_stack = []
    temp_list = []
    # for i in so:
    #     if i.isdigit():
    #         temp_list.append(i)
    #     elif i.isalpha():
    #         temp_list.append(variable_storage[i])
    #     # elif i == "("
    #     elif i in ("+", "-", "*", "/"):
    #         temp_stack.append(i)
    #     elif i == ")":
    #         while temp_stack:
    #             temp_list.append(temp_stack.pop())
    # while temp_stack:
    #     temp_list.append(temp_stack.pop())
    # res = run_postfix(temp_list)
    # return res
    so = ui_in_list(so)
    for i in so:
        # Добавляйте операнды (числа и переменные) к
        # результату (постфиксная запись) по мере их поступления.
        if i.isdigit():
            temp_list.append(i)
        elif i in variable_storage:
            temp_list.append(variable_storage[i])
        # Если стек пуст или содержит левую круглую скобку наверху,
        # поместите входящий оператор в стек.
        elif i in ("+", "-", "//", "*"):
            if len(temp_stack) == 0 or temp_stack[-1] == "(":
                temp_stack.append(i)
        # Если входящий оператор имеет более высокий приоритет,
        # чем вершина стека, поместите его в стек.
            elif i in ("//", "*") and temp_stack[-1] in ("+", "-"):
                temp_stack.append(i)
        # Если входящий оператор имеет более низкий или равный приоритет,
        # чем или вверху стека, вытяните стек и добавляйте операторы
        # к результату, пока не увидите оператор с меньшим приоритетом
        # или левую скобку наверху стека; затем добавьте в стек входящий
        # оператор.
            # если приоритет ниже
            elif i in ("+", "-") and temp_stack[-1] in ("//", "*"):
                # имеет низкий приоритет
                while len(temp_stack) and temp_stack[-1] != "(":
                    temp_list.append(temp_stack.pop())
                temp_stack.append(i)

            # если приоритет равен
            elif i in ("+", "-") and temp_stack[-1] in ("+", "-"):
                while len(temp_stack) and temp_stack[-1] != "(":
                    temp_list.append(temp_stack.pop())
                temp_stack.append(i)
            elif i in ("*", "//") and temp_stack[-1] in ("//", "*"):
                while len(temp_stack) and temp_stack[-1] != "(":
                    temp_list.append(temp_stack.pop())
                temp_stack.append(i)
        # Если входящий элемент является левой круглой скобкой,
        # поместите его в стек.
        elif i == "(":
            temp_stack.append(i)
        # если входящий элемент является правой круглой скобкой,
        # вытяните стек и добавляйте операторы к результату,
        # пока не увидите левую скобку. Отбросьте пару круглых скобок.
        elif i == ")":
            while temp_stack[-1] != "(":
                temp_list.append(temp_stack.pop())
            temp_stack.pop()
        # В конце выражения вытолкните стек и добавьте
        # все операторы к результату
    while temp_stack:
        temp_list.append(temp_stack.pop())
    run_postfix(temp_list)


def run_postfix(so):
    st = []
    tl = []
    for i in so:
        if i.isdigit():
            st.append(int(i))
        elif i in ("+", "-", "*", "/"):
            x = st[-1]
            print(x)
            st = st[:-1]
            print(st)
            y = st[-1]
            print(y)
            st = st[:-1]
            print(st)
            if i == "+":
                st.append(x+y)
            elif i == "-":
                st.append(x-y)
            elif i == "*":
                st.append(x*y)
            elif i == "/":
                st.append(x//y)
        # elif i == ")":
        #     while st:
        #         tl.append(st.pop())
    # while st:
    #     tl.append(st.pop())
    print(temp_stack[0])


exit_flag = 1

while exit_flag:
    ui = input()
    # try:
    #     ui = input()
    # except:
    #     print("Invalid assignment")
    while " " in ui or "++" in ui or "--" in ui or "+-" in ui or "-+" in ui:
        ui = ui.replace(" ", '')
        ui = ui.replace("++", "+")
        # ui = ui.replace("+++","+")
        ui = ui.replace("--", "+")
        ui = ui.replace("+-", "-")
        ui = ui.replace("-+", "-")
    ui = ui.replace("/", "//")




    # try:
    #     eval(ui)
    #     ui = input()
    # except:
    #     pass
    if ui.startswith(')'):
        print("Invalid expression")
        continue
    elif (ui.count("(") - ui.count(")")) != 0:
        print("Invalid expression")
        continue
    elif ui.endswith("("):
        print("Invalid expression")
        continue
    elif "**" in ui or "////" in ui:
        print("Invalid expression")
        continue
    elif ui.isdigit():
        print(ui)
        continue
    elif ui.startswith('-') and ui[1:].isdigit():
        print(ui)
        continue
    elif ui == '':
        continue
    elif ui.startswith("/"):
        if ui == "/exit":
            print("Bye!")
            exit_flag = 0
        elif ui == "/help":
            print("This is a HELP")
            continue
        else:
            print("Unknown command")
            continue
    elif "=" in ui:
        ss = ui.split("=")  # разбить строку по =
        ss = [i.strip() for i in ss]  # обрезать все
        if ss[0] in variable_storage and ss[1].isdigit():  # переприсваивание
            variable_storage[ss[0]] = ss[1]
            continue
        elif ss[0].isalpha() and \
                ss[0] not in variable_storage and \
                ss[1].isdigit():  # буква не в переменных = цифра новая перемен
            variable_storage[ss[0]] = ss[1]
            continue
        elif ss[0].isalpha() and \
                ss[1].isalpha() and \
                ss[1] in variable_storage:  # буква = буква в переменных
            variable_storage[ss[0]] = variable_storage[ss[1]]
            continue
        elif ss[0].isalpha() and \
                ss[1].isalpha() and \
                ss[1] not in variable_storage:  # буква = буква не в переменных
            print("Unknow variable")
            continue
        elif ss[0].isdigit() and ss[1].isdigit():  # цифра равна цифре
            print("Invalid assignment")
            continue
    elif all_isalpha(ui):
        if ui in variable_storage:
            print(variable_storage[ui])
        else:
            print("Unknow variable")
    else:
        create_postfix(ui)

print(run_postfix(ui))
