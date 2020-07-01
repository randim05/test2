i = input()
if i:
    i = int(i)
    if i == 1:
        print("This number is not prime")
    if i >= 2:
        for x in range(2, i + 1):
            if i == x:
                print("This number is prime")
                break
            if i % x == 0:
                print("This number is not prime")
                break