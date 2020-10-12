# import sys
#
# args = {i: j for x.split("=") in sys.argv[1:]}
# print(args)


import math
import sys
# args = ["python", "sys_arg_unpak1.py", "--type=diff", "--principal=500000", "--periods=8", "--interest=7.8"]

args = ["python", "creditcalc.py", "--type=annuity", "--principal=1000000", "--periods=60", "--interest=10"]

arg_dict = {'type': 0, "payment": 0, "principal": 0, "periods": 0, "interest": 0}
main_loop_flag = True
while main_loop_flag:
    for i in args:
        if i.startswith("--type"):
            arg_dict["type"] = i.split("=")[1]
        elif i.startswith("--payment"):
            arg_dict["payment"] = int(i.split("=")[1])
        elif i.startswith("--principal"):
            arg_dict["principal"] = int(i.split("=")[1])
        elif i.startswith("--periods"):
            try:
                arg_dict["periods"] = int(i.split("=")[1])
            except ValueError:
                print("Incorrect parameters")
                main_loop_flag = False
                break
            if arg_dict["periods"] < 0:
                print("Incorrect parameters")
                main_loop_flag = False
                break
        elif i.startswith("--interest"):
            try:
                arg_dict["interest"] = int(i.split("=")[1])
            except ValueError:
                arg_dict["interest"] = float(i.split("=")[1])
            if arg_dict["interest"] <= 0:
                print("Incorrect parameters")
                main_loop_flag = False
                break
            arg_dict["interest"] = arg_dict["interest"] / 1200

    pay_type = arg_dict["type"]
    principal = arg_dict["principal"]
    periods = arg_dict["periods"]
    interest = arg_dict["interest"]
    payment = arg_dict["payment"]

    if pay_type == "diff" and payment:
        print("Incorrect parameters")
        main_loop_flag = False
        break
    if periods < 0:
        print("Incorrect parameters")
        main_loop_flag = False
        break
    if len(args) < 5:
        print("Incorrect parameters")
        main_loop_flag = False
        break

    if pay_type == "diff" and principal and periods and interest and not payment:
        now_month = 1
        sum_pay = 0
        while now_month <= periods:
            dif_pay = math.ceil(principal / periods + interest * (principal - (principal * (now_month - 1)) / periods))
            print(f'Month {now_month}: payment is {dif_pay}')
            now_month += 1
            sum_pay += dif_pay
        print()
        print(f'Overpayment = {int(sum_pay - principal)}')
        main_loop_flag = False
        break
    if pay_type == "annuity":
        if payment and periods and interest and not principal:
            principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
            print(f'Your loan principal = {int(principal)}!')
            print(f'Overpayment = {int(payment * periods - principal)}')
            main_loop_flag = False
            break
        elif principal and payment and interest and not periods:
            n = math.log(payment / (payment - interest * principal), 1 + interest)
            if n % 10 == 0:
                pass
            else:
                n = int(n) + 1
            if n % 12 == 0:
                print("It will take " + str(n / 12) + " years to repay this loan!")
            elif n / 12 < 1:
                print("It will take " + str(n) + " months to repay this loan!")
            else:
                print("It will take " + str(n // 12) + " years and " + str(n % 12) + " months to repay this loan!")
            print(f'Overpayment = {payment * periods - principal}')
            main_loop_flag = False
            break
        elif principal and periods and interest and not payment:
            # n = math.log(payment / (payment - periods * principal), 1 + i)
            aut = principal * ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
            print(f'Your annuity payment = {round(aut)}!')
            print(f'Overpayment = {round(aut) * periods - principal}')

            main_loop_flag = False
            break

