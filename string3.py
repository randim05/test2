# a = 1
# name = 'meee'
# print(f'my {a} name is {name}')
# print('{t} in {z}'.format(t=name, z=a))


x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)