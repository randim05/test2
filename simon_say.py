def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return "I " + instructions[11:]
    if instructions.endswith("Simon says"):
        return "I " + instructions[:-10]
    else:
        return "I won't do it!"


print(what_to_do("Simon says hello world!"))
print(what_to_do("hello world! Simon says"))
print(what_to_do("hello world!"))
print(what_to_do("hello Simon says world! "))