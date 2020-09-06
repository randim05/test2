ui = '1+2*((3+4)*5+6)-7/(8+9)'
# var_stor = {'a':'5', 'bc': '6', '6c':'7'}
# DIGITS = "1234567890"
# ZNAKS = "+-*/"
# letters = []
# digits = []
# math_symbols = []
# result = []
#
# for i in ui:
#     if i in DIGITS:                                          # if coming digit
#         if len(letters) != 0:  # or len(math_symbols) == 0:      # was alphas and not math_zn
#             print("Invalid variables " + ''.join(letters))                       # digit after symbol not valid variable)
#             break
#         digits.append(i)  # and go create next digit
#
#     elif i.isalpha():  # if coming alphas
#         if len(digits) != 0:  # a was digits or no math_zn
#             print("Invalid expression " + i)
#             break
#         elif len(math_symbols) != 0:
#             result.append(''.join(math_symbols))
#             math_symbols = []
#         letters.append(i)
#     elif i == ' ':
#         continue
#     elif i in ZNAKS:
#         if len(digits) != 0:
#             result.append(''.join(digits))
#             digits = []
#         elif len(letters) != 0:
#             x = ''.join(letters)
#             if x in var_stor:
#                 result.append(var_stor[x])
#             else:
#                 print("Invalid variables " + x)
#                 break
#             letters = []
#         result.append(i)
#     # elif i == ')' and len(bracket) == 0:
#     #     return "Invalid expression"
#     else:
#         result.append(i)
#     # elif ui.starstwhith(")"):
#     #     return "Invalid expression"
# print(result)

quere = []
stack = []
for i in ui:
    if i.isdigit():
        quere.append(i)
    elif i in ("+", "-", "*", "/", "(") and (len(stack) == 0 or stack[-1] == '('):  #not in ("(", "*", "/"):
        stack.append(i)
    elif i in ("+", "-") and stack[-1] in ("+", "-", "("):
        stack.append(i)
    elif i in ("*", "/") and stack[-1] in ("(", "+", "-"):
        stack.append(i)
    elif i in ("*", "/") and stack[-1] in ("(", "*", "/"):
        stack.append(i)
    elif i in ("+", "-") and stack[-1] in ("*", "/"):
        quere.append(stack.pop())
        while len(stack) != 0 or stack[-1] not in ("(", "*", "/"):
            quere.append(stack.pop())
        stack.append(i)
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack[-1] != '(':
            quere.append(stack.pop())
        stack.pop()
    elif i == " ":
        continue
while stack:
    quere.append(stack.pop())

print(quere)