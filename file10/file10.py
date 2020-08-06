# write your code here
for i in range(1, 11):
    with open('file%s.txt' % str(i), 'w') as f:
        print(i, file=f, end='')