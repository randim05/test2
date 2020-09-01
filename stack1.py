n = int(input())
my_stack = []

while len(my_stack) < n:
    my_stack.append(input().strip())

while len(my_stack):
    print(my_stack.pop())
