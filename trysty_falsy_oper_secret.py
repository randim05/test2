
def hidden_operation(operand):
    if oper == "and":
        return operand and hidden_operand
    elif oper == "or":
        return operand or hidden_operand
    elif oper == "not":
        return not operand


def solve():
    if hidden_operation('123') and hidden_operation('123') != '123' and hidden_operation('') == '':
        print('and')
        print(hidden_operation('123'))  # Truthy
    elif not hidden_operation('123') and hidden_operation('123') != '123' and hidden_operation('') == '':
        print('and')
        print(hidden_operation('123')) # Falsy

    elif hidden_operation('123') == '123' and hidden_operation('') and hidden_operation('') != '':
        print('or')
        print(hidden_operation('')) # Truthy
    elif hidden_operation('123') == '123' and not hidden_operation('') and hidden_operation('') != '':
        print('or')
        print(hidden_operation('')) # Falsy

    elif hidden_operation('123') == False and hidden_operation('') == True:
        print('not')
