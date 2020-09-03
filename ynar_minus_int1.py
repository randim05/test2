# a = '-10'
# print(int(a))
# print(a.isdigit())
ui = input()
ef = 1
while ef:
    if ui.isdigit():
        print(ui)
        ui = input()
        continue
    elif ui.startswith('-') and ui[1:].isdigit():
        print(ui)
        ui = input()
        continue
