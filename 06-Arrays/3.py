#Create a program that computes the second power of each array element. Sample result:
#Array: 8 2 5 1 9
#2nd power: 64 4 25 1 81

def f():
    arr=[8,2,5,1,9]
    arr2=[]
    for i in range(len(arr)):
        arr2.append(arr[i]*arr[i])
    return arr2
print(f())

