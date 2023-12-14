#An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and displays the maximum and minimum number. 
# Do not use available functions.

def f():
    arr=[-15, 8, -31, 47, -2, 19]
    # Initialize variables to store maximum and minimum values
    max_number = arr[0]  # Assume the first number is the maximum
    min_number = arr[0]  # Assume the first number is the minimum

    # Iterate through the array to find maximum and minimum values
    for num in arr:
        # Check for maximum value
        if num > max_number:
            max_number = num
        
        # Check for minimum value
        if num < min_number:
            min_number = num
    return max_number, min_number

print(f())