def bubblesort(array):
    # Get the length of the array
    n = len(array)

    # Traverse through all elements in the array
    for i in range(n - 1):
        # Flag to check if any swapping occurs in this iteration
        swapped = False

        # Last i elements are already in place after (i+1) iterations
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1, swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # If no two elements were swapped in the inner loop, array is already sorted
        if not swapped:
            break

    return array

# Example arrays
array1 = [64, 25, 12, 22, 11]
array2 = [38, 27, 43, 3, 9, 82, 10]
array3 = [5, 2, 9, 1, 5, 6]

# Sort and display the three arrays using Bubble Sort
sorted_array1 = bubblesort(array1.copy())
sorted_array2 = bubblesort(array2.copy())
sorted_array3 = bubblesort(array3.copy())

print("Original array 1:", array1)
print("Sorted array 1:", sorted_array1)

print("\nOriginal array 2:", array2)
print("Sorted array 2:", sorted_array2)

print("\nOriginal array 3:", array3)
print("Sorted array 3:", sorted_array3)