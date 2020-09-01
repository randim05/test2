n = int(input())
stack_list = []
sch = 0
while sch < n:
    im = input().split(" ")
    sch += 1
    if im[0] == "PUSH":
        stack_list.append(int(im[1]))
    elif im[0] == "POP":
        stack_list.pop()

while stack_list:
    print(stack_list.pop())