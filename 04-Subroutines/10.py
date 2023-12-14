def f(number, even):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    # Initialize the sum of even/odd digits
    digit_sum = 0

    # Iterate through each digit in the number
    for digit_char in number_str:
        digit = int(digit_char)

        # Check if the digit is even or odd based on the 'even' parameter
        if (digit % 2 == 0 and even) or (digit % 2 != 0 and not even):
            digit_sum += digit  # Add the digit to the sum

    return digit_sum
# Sample usage:
print("f(3124,True) returns:", f(3124, True))
print("f(3124,False) returns:", f(3124, False))
print("f(20576,False) returns:", f(20576, False))
print("f(20576,True) returns:", f(20576, True))
print("f(13115,True) returns:", f(13115, True))