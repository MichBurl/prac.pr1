#A two-dimensional array contains the same number of rows and columns. 
# Create a function f(array2D) that, for the given two-dimensional array array2D, 
# returns True when the sum of the values in each row of the array is equal to the sum of the values in the corresponding column 
# (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) , and False otherwise. Example:
#f([[3,7,2],[4,2,5],[5,2,1]])  True
#f([[3,7,2],[4,2,5],[9,2,1]])  False

def f(array2D):
    # Check if the array is square (number of rows == number of columns)
    if len(array2D) != len(array2D[0]):
        return False

    size = len(array2D)
    
    # Calculate sums of rows and columns
    row_sums = [sum(row) for row in array2D]
    col_sums = [sum(array2D[i][j] for i in range(size)) for j in range(size)]

    # Compare row sums and column sums
    return row_sums == col_sums

# Test cases
print(f([[3, 7, 2], [4, 2, 5], [5, 2, 1]]))  # Expected output: True
print(f([[3, 7, 2], [4, 2, 5], [9, 2, 1]]))  # Expected output: False
