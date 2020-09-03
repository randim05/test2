
variable_storage = {}
def create_postfix(so):
    temp_stack = []
    temp_list = []
    for i in so:
        if i.isdigit():
            temp_list.append(i)
        elif i.isalpha():
            temp_list.append(variable_storage[i])
        elif i in ("+", "-", "*", "/"):
            temp_stack.append(i)
        elif i == ")":
            while temp_stack:
                temp_list.append(temp_stack.pop())
    while temp_stack:
        temp_list.append(temp_stack.pop())
    res = run_postfix(temp_list)
    return res


def run_postfix(so):
    st = []
    tl = []
    for i in so:
        if i.isdigit():
            st.append(i)
        elif i in ("+", "-", "*", "/"):
            x = st.pop()
            y = st.pop()
            z = eval(x+i+y)
            st.append(str(z))
        # elif i == ")":
        #     while st:
        #         tl.append(st.pop())
    # while st:
    #     tl.append(st.pop())
    return int(st[0])


exit_flag = 1

while exit_flag:
    try:
        ui = input()
    except:
        print("Invalid assignment")
    while " " in ui or "++" in ui or "--" in ui or "+-" in ui or "-+" in ui:
        ui = ui.replace(" ", '')
        ui = ui.replace("++","+")
        # ui = ui.replace("+++","+")
        ui = ui.replace("--","+")
        ui = ui.replace("+-","-")
        ui = ui.replace("-+", "-")

    if ui.startswith(')'):
        print("Invalid expression")
        continue
    elif (ui.count("(") - ui.count(")")) != 0:
        print("Invalid expression")
        continue
    elif ui.endswith("("):
        print("Invalid expression")
        continue
    elif "**" in ui or "//" in ui:
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
        ss = ui.split("=")
        ss = [i.strip() for i in ss]
        if ss[0] in variable_storage and ss[1].isdigit():
            variable_storage[ss[0]] = ss[1]
            continue
        elif ss[0].isalpha() and ss[0] not in variable_storage and ss[1].isdigit():
            variable_storage[ss[0]] = ss[1]
            continue
        elif ss[0].isalpha() and ss[1].isalpha() and ss[1] in variable_storage:
            variable_storage[ss[0]] = variable_storage[ss[1]]
            continue
        elif ss[0].isalpha() and ss[1].isalpha() and ss[1] not in variable_storage:
            print("Unknow variable")
            continue
    elif ui.isalpha():
        if ui in variable_storage:
            print(variable_storage[ui])
        else:
            print("Unknow variable")
    else:
        print(create_postfix(ui))

