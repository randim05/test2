# a = 1
# name = 'meee'
# print(f'my {a} name is {name}')
# print('{t} in {z}'.format(t=name, z=a))


x = 50


def func(x):
    """this is triple quote text. i doc for func(x) function"""
    print('local x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('but global x is still', x)
print(func.__doc__)

if __name__ == '__main__':
    print("i am start as modul")
else:
    print("i was imported")
