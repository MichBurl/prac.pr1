import random

def rand_elem(array):
    # Generate a random index within the range of the array length
    random_index = random.randint(0, len(array) - 1)
    
    # Return the element at the randomly generated index
    return array[random_index]

# Sample array
my_array = [10, 20, 30, 40, 50, 60, 70]

# Displaying a few randomly selected array elements using the rand_elem() function
for _ in range(3):  # Displaying 3 randomly selected elements
    random_element = rand_elem(my_array)
    print("Randomly selected element:", random_element)