# a = [1, 2, 3, 4, 5]
# a.sort(reverse=True)
# print(a)

for i in range(10):
    print(i, end=" ")
    for y in "abcdefghijklmnopqrstuvwxyz":
        if y == 'e':
            break
        if y == 'b':
            continue
        print(y, end=" ")
    if i == 3:
        break
