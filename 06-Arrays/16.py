def flatten_2d_to_1d(arr_2d):
    # Initialize an empty 1D array
    arr_1d = []

    # Iterate through each row of the 2D array and append elements to the 1D array
    for row in arr_2d:
        arr_1d.extend(row)

    return arr_1d

# Given 2D arrays
arrays_2d = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5]],
    [[7, 4], [2, 6]]
]

# Display 1D arrays for each 2D array
for i, arr_2d in enumerate(arrays_2d):
    arr_1d = flatten_2d_to_1d(arr_2d)
    print(f"1D Array for 2D Array {i+1}: {arr_1d}")