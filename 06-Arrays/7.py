#Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that displays the numbers from the first array that do not appear in the second array.
def f():
    arr1=[4,36,12,28,9,44,5]
    arr2=[5,1,36]
    arr3=[]
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            arr3.append(arr1[i])
    return arr3
print(f())