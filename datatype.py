


def separate_types(*args):
   
    integers = []
    floats = []
    strings = []
    invalid_inputs = []

    for arg in args:
        if isinstance(arg, int):
            integers.append(arg)
        elif isinstance(arg, str):
            strings.append(arg)
        elif isinstance(arg, float):
            floats.append(arg)
        else:
            invalid_inputs.append(arg)

    if invalid_inputs:
        print("Invalid inputs:", invalid_inputs)

    return integers, floats, strings

integers, floats, strings = separate_types(1, 2, 3, 3, 4.0, "a", "b")

print("The integers are :", integers)
print("The floats are :", floats)
print("The strings are :", strings)


