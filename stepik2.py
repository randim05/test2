lst = [int(i) for i in input().split()]
a = int(input())
res = []
poz = 0
for i in lst:
    if i == a:
        res.append(poz)
    poz += 1
if a not in lst:
    print("Отсутствует")
for i in res:
    print(i, end=' ')