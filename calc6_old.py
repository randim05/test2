ui = input()
bank = {}
def do_postfix(so):
    st = []
    tl = []
    for i in so:
        if i.isdigit():
            tl.append(int(i))
        elif i.isalpha():
            tl.append(bank[i])
        elif i in ("+", "-", "*", "/"):
            st.append(i)
        elif i == ")":
            while st:
                tl.append(st.pop())
    while st:
        tl.append(st.pop())
    run_postfix(tl)


def run_postfix(so):
    st = []
    tl = []
    for i in so:
        if i.isdigit():
            st.append(int(i))
        elif i in ("+", "-", "*", "/"):
            x = tl.pop()
            y = tl.pop()
            z = eval(x+i+y)
            st.append(z)
        # elif i == ")":
        #     while st:
        #         tl.append(st.pop())
    # while st:
    #     tl.append(st.pop())
    return st.pop()


exit_flag = 1

while exit_flag:
    ui = ui.replace(" ", '')
    ui = ui.replace("++","+")
    ui = ui.replace("+++","+")
    ui = ui.replace("--","+")
    ui = ui.replace("---","-")

    if ui.startswith(')'):
        print("Invalid expression")
        ui = input()
        continue
    elif (ui.count("(") - ui.count(")")) != 0:
        print("Invalid expression")
        ui = input()
        continue
    elif ui.endswith("("):
        print("Invalid expression")
        ui = input()
        continue
    elif "**" in ui or "//" in ui:
        print("Invalid expression")
        ui = input()
        continue
    elif ui.isdigit():
        print(ui)
        ui = input()
        continue
    elif ui.startswith('-') and ui[1:].isdigit():
        print(ui)
        ui = input()
        continue
    elif ui == '':
        ui = input()
        continue
    elif ui.startswith("/"):
        if ui == "/exit":
            print("Bye!")
            exit_flag = 0
        elif ui == "/help":
            print("This is a HELP")
            ui = input()
            continue
        else:
            print("Unknown command")
            ui = input()
            continue
    elif "=" in ui:
        ss = ui.split("=")
        ss = [i.strip() for i in ss]
        if ss[0] in bank and ss[1].isdigit():
            bank[ss[0]] = ss[1]
            ui = input()
            continue
        elif ss[0].isalpha() and ss[0] not in bank and ss[1].isdigit():
            bank[ss[0]] = ss[1]
            ui = input()
            continue
        elif ss[0].isalpha() and ss[1].isalpha() and ss[1] in bank:
            bank[ss[0]] = bank[ss[1]]
            ui = input()
            continue
        # elif ss[0].isalpha() and ss[1].isalpha() and ss[1] not in bank:
        else:
            print("Unknow variable")
            ui = input()
            continue
    else:
        print(do_postfix(ui))
        ui = input()
