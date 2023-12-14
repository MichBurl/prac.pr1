#Create a function f(first_letter,last_letter) that, for the data.txt file, 
# returns the number of words that start with the first_letter and end with the last_letter. Example:
#f("w","d") 🡪 compare your result with other students

def f(first_letter, last_letter):
    # Open the file for reading
    with open('E:\\GitHub\\pp1\\09-Test2\\dataa.txt', 'r') as file:
        # Read the file content
        content = file.read()

        # Split the content into words
        words = content.split()

        # Count words starting with first_letter and ending with last_letter
        count = sum(1 for word in words if word.startswith(first_letter) and word.endswith(last_letter))

    return count

# Call the function with specified letters
result = f('w', 'd')
print(f"Number of words starting with 'w' and ending with 'd': {result}")