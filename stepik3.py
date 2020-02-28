import copy

y = 1
a = []
while y:
    x = input()
    if x != 'end':
        a.append([int(i) for i in x.split(' ')])
    else:
        y = 0
# print(a)
# b=[i[j for j in range(len(a[i]))] for i in range(len(a))]
b = copy.deepcopy(a)
# for i in b:
#     for j in i:
#         j = 0
# print(b)
# print(b is a)
# print(len(a))
# print(len(a[0]))
for i in range(len(a)):
    for j in range(len(a[i])):
        # for di in (-1, 1):
        #     for dj in (-1, 1):
                right = a[i][j + 1 - len(a[i])]
                left = a[i][j - 1]
                up = a[i - 1][j]
                down = a[i + 1 - len(a)][j]
                b[i][j] = left + right + down + up
# for i in b:
#     print(' '.join(i))
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
    print()