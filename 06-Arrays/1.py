#An array contains integer numbers: 34,7,19,4,21,8. 
# Create a program that calculates and displays the number of even values in the array. 
# Use the ‘while’ loop statement.

def f():
    arr=[34,7,19,4,21,8]
    ev=[]
    i=0
    while i<len(arr):
        if arr[i]%2==0:
            ev.append(arr[i])
        i+=1
    return (sum(ev))
#   return (len(ev))

print(f())


