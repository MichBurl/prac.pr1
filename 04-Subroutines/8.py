def f(binary_number):
    return all(char in '01' for char in binary_number)
print(f("1011011"))