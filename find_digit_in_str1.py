
a = 'a3b4c2e10b1'
res = []
tmp = []
for i in a:
    try:
        x = int(i)
        tmp.append(x)
    except ValueError:
        # res.append(str(''.join(tmp)))
        if len(tmp) != 0:
            # for j in tmp:
            #     j = str(j)
            res.append(''.join(map(str, tmp)))
        tmp = []
    # else:

for i in res: print(i, end=' ')
