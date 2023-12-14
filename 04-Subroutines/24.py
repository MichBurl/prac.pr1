def f(password):
    # Check if the length of the password is at least 6 characters
    if len(password) < 6:
        return False

    # Convert the password to a set to count unique characters
    test = list(password)
    unique_chars = set(password)
    if(len(test)!=len(unique_chars)): return False
    else: return len(unique_chars) >= 6
    # Check if the number of unique characters is at least 6
print(f("A2water3"))