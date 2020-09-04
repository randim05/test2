ui = input()


def do_postfix(so):
    st = []
    tl = []
    for i in so:
        if i.isdigit():
            tl.append(i)
        elif i in ("+", "-", "*", "/"):
            st.append(i)
        elif i == ")":
            while st:
                tl.append(st.pop())
    while st:
        tl.append(st.pop())
    print(tl)
    run_postfix(tl)


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
                st.append(x/y)
        # elif i == ")":
        #     while st:
        #         tl.append(st.pop())
    # while st:
    #     tl.append(st.pop()) urt 1lI g --> ==>

    return st


print(do_postfix(ui))