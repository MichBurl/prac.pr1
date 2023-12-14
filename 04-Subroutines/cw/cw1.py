def phone_keyboard():
    number = 1
    for row in range(3):
        for col in range(3):
            print(number, end=' ')
            number += 1
        print()  # Move to the next line after printing each row

# Call the function
phone_keyboard()
