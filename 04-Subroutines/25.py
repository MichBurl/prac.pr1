def f(expression):
    result = 0
    num = ''
    operator = '+'

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if operator == '+':
                result += int(num)
            else:
                result -= int(num)
            operator = char
            num = ''

    if operator == '+':
        result += int(num)
    else:
        result -= int(num)

    return result

# Test cases:
print("f('2+3') returns:", f("2+3"))  # Output: 5
print("f('3+8+1') returns:", f("3+8+1"))  # Output: 12
print("f('2+3-4+5-0') returns:", f("2+3-4+5-0"))  # Output: 6
