def sum_repeated_digits(number):
    # Convert the number to a string for easier manipulation
    num_str = str(number)
    
    # Dictionary to store counts of each digit
    digit_count = {}
    
    # Iterate through each digit in the number
    for digit in num_str:
        if digit.isdigit():
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
    
    # Calculate the sum of repeated digits
    repeated_sum = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)
    
    return repeated_sum

# Test cases:
print("f(1027) returns:", sum_repeated_digits(1027))  # Output: 0
print("f(230335) returns:", sum_repeated_digits(230335))  # Output: 9
print("f(513553007) returns:", sum_repeated_digits(513553007))  # Output: 21
