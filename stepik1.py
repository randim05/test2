a = int(input())
# l = [0 for i in range(a)]
l = []
for i in range(1, a+1):
    j = 0
    while j < i:
        l.append(i)
        j += 1
for i in l[:a]:
    print(i, end=' ')
