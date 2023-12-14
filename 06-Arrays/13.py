#An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
# Create a program that finds the smallest and largest values in the array and in which row and column they are located.

def f():
    # Given array
    array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

    # Initialize variables for smallest and largest values, row, and column indices
    smallest_value = float('inf')
    largest_value = float('-inf')
    smallest_position = (0, 0)
    largest_position = (0, 0)

    # Iterate through the array to find smallest and largest values
    for i, row in enumerate(array):
        for j, value in enumerate(row):
            if value < smallest_value:
                smallest_value = value
                smallest_position = (i, j)
            if value > largest_value:
                largest_value = value
                largest_position = (i, j)
    return largest_position,largest_value,smallest_position,smallest_value

print(f())