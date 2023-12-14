# Create a 3x5 two-dimensional array with integer numbers
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Display array values before changes
print("Array before swapping:")
for row in array:
    print(row)

# Swap the first and last columns
for row in array:
    row[0], row[-1] = row[-1], row[0]

# Display array values after swapping columns
print("\nArray after swapping:")
for row in array:
    print(row)