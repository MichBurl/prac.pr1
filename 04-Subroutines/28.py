def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    first_three_digits = int(product_code[:3])
    control_digit = int(product_code[-1])

    return first_three_digits % 7 == control_digit
print(f("1082"))