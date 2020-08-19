def check(obj1, obj2):
    if id(obj1) == id(obj2):
        return True
    else:
        return False
print(check(1, 1))
print(check([1], [213123]))
a = [1]
b = a
print(check(a, b))
x = [1]
y = [1]
print(check(x, y))
print(check('a', 'a'))
print(check('a', 'b'))
r = 'a'
y = 'a'
print(check(r, y))