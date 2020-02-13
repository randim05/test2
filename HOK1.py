# наименьшее общее кратное

# put your python code here
a = int(input())
b = int(input())
s = True
for i in range(1, 1000):
    if (a * i) % b == 0:
        print(a * i)
        break

# not my

a = int(input())
b = int(input())
d = a
while d % b != 0:
    d += a
print(d)
