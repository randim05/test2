# def fib(x):
#     # res = []
#     a = 0
#     b = 1
#     for __ in range(x):
#         a, b = b, a + b
#     # res.append(a)
#     return a
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

x = 4
r = []
i = 0

while len(r) < x:
    m = fib(i)
    i += 1
    if m % 2 == 0:
        r.append(m)
print(r)
#
# print(r)
# some_res = []
# for i in r:
#     if i % 2:
#         some_res.append(i)
#
# print(" ".join(some_res))



# x = [i for i in fib(4) if i % 2 == 0]

