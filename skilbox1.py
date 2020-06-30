def max_num(a):
    x = 0
    max1 = 0
    try:
        for i in a:
            if i > x:
                max1 = i
    except Exception as exc: print(exc)

