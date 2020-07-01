a = int(input())
b = int(input())
x = 0
res = 0
for i in range(a, b+1):
    if i % 3 == 0:
        x += 1
        res += i
print(res / x)
# for i in range(a, b+1):
#     if i % 3 == 0:
#         print(i)