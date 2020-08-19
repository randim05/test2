def tallest_people(**arg):
    c = dict(arg)
    max = []
    for i in c:
        if not max:
            max.append(i)
        else:
            if arg[i] > arg[max[0]]:
                max = []
                max.append(i)
            elif arg[i] == arg[max[0]]:
                max.append(i)
    for u in max:
        print(f'{u} : {arg[u]}')


tallest_people(Jackie=176,
               Wilson=185,
               Saersha=165,
               Roman=185,
               Abram=169)
