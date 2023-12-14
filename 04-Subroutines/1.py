#mymath.py
import random

def generate_number():
    return random.randint(1, 9)

#main_program.py
def main():
    user_number = input("Enter a number: ")
    computer_number = generate_number()

    print("Computer number:", computer_number)

    if user_number == computer_number:
        print("You won the game!!")
    else:
        print("You lost. Try again!")

if __name__ == "__main__":
    main()