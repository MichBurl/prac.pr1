#An array contains at least 3 integers. All numbers in the array are equal except one. 
# Create a function f(arr) that returns a number in the arr array that is different from the other numbers. Example:
#f([7,7,7,7,7,5,7,7])  5

def f(arr):
    for i in range(len(arr)):
        if arr[i]!=arr[i+1]: return arr[i+1]

print(f([7,7,7,7,7,2,7,7]))
