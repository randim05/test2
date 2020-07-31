while True:
    x = float(input())
    y = float(input())
    s = input()
    if s == '+':
        print("%.1f" % (x + y))
    elif s == '-':
        print("%.1f" % (x - y))
    elif s == '*':
        print("%.1f" % (x * y))
    elif s == 'pow':
        print("%.1f" % (x ** y))
    elif s == 'mod':
        if y:
            if (x % y) < 0 or -0.0:
                print("%.1f" % ((x % y) * (-1.0)))
                # print("%.1f" % (x % y))
            else:
                print("%.1f" % (x % y))
        else:
            print("Division by 0!")
    elif s == 'div':
        if y:
            print("%.1f" % (x // y))
        else:
            print("Division by 0!")
    elif s == '/':
        if y:
            print("%.1f" % (x / y))
        else:
            print("Division by 0!")