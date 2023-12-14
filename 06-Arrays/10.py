#Write a program that checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array)

def f():
    arr1=[1,2,3,5]
    arr2=[7,6,5,4,3,2]
    arr3=[]
    for element in arr1:
        if element in arr2:
            arr3.append(element)
    if arr3==arr1:
        return True
    else: return False
print(f())