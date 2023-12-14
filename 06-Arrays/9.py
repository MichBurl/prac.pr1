#Create a program that displays all unique elements in an array. Sample result:
#Array: 2 3 2 5 8 1 9 8
#Unique elements: 3 5 1 9

def f():
    arr=[2, 3, 2, 5, 8, 1, 9, 8]
    unique_elements = []

    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)

    return unique_elements

print(f())
