n = int(input())
queue = []

while n:
    ui = input().split(" ")
    if ui[0] == "READY":
        queue.append(ui[1])
        n -= 1
    elif ui[0] == "EXTRA":
        x = queue[0]
        queue = queue[1:]
        queue.append(x)
        n -= 1
    elif ui[0] == "PASSED":
        print(queue[0])
        if queue:
            queue = queue[1:]
        n -= 1