import math
print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')
ui = input()
if ui == 'n':
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the monthly payment:")
    payment = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    if n % 10 == 0:
        pass
    else:
        n = int(n) + 1
    if n % 12 == 0:
        print("It will take " + str(n / 12) + " years")
    elif n / 12 < 1:
        print("It will take " + str(n) + " months")
    else:
        print("It will take " + str(n // 12) + " years and " + str(n % 12) + " months to repay this loan!")
elif ui == 'a':
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the number of periods:")
    month = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    aut = principal * ((i * (1 + i) ** month) / ((1 + i) ** month - 1))
    print(int(aut) + 1)
elif ui == 'p':
    print("Enter the annuity payment:")
    aut = float(input())
    print("Enter the number of periods:")
    month = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    principal = aut / ((i * (1 + i) ** month) / ((1 + i) ** month - 1))
    print(int(principal))
