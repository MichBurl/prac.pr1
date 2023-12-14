def f(palindrome):
    # Remove non-alphanumeric characters and convert to lowercase
    palindrome = ''.join(char.lower() for char in palindrome if char.isalnum())
    print(palindrome[::-1])
    
    # Check if the string equals its reverse
    return palindrome == palindrome[::-1]
print(f('test'))