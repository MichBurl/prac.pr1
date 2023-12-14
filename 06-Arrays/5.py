#An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “for” loop statement.

def f():
    # Define the array
    values = [15, 8, 31, 47, 2, 19]

    # Calculate the sum of array values
    sum_values = 0
    for value in values:
        sum_values += value

    # Calculate the arithmetic mean
    array_length = len(values)
    arithmetic_mean = sum_values / array_length

    return values,arithmetic_mean
print(f())
