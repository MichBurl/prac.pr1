def check(x,y):
    number=int(input("Enter a number:"))
    print(f"Number {number} is in range <{x},{y}>:")
    return x<number<y

def main():
    if(check(2,12)):
        print("yes")
    else:
        print("no")
main()