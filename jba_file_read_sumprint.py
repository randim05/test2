with open('sums.txt', 'r') as f:
    for i in f:
        i = i.strip()
        s = i.split(' ')
        # print(s)
        print(int(s[0]) + int(s[1]))