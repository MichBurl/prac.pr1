#An array contains values: [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
# Create a program that modifies the array values to create a multiplication table as below. Use loop statements. Display the array.
#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20
#5 10 15 20 25

def f():
    arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(len(arr)):
        arr[i][0]=i+1
        for j in range(len(arr)):
            arr[i][j]=(i+1)*(j+1)
    return arr
print(f())



