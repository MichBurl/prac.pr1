def check(n1,n2,n3):
    if(n1==n2==n3):
        return False
    else:
        return True

n1=input("Enter first number: ")
n2=input("Enter second number: ")
n3=input("Enter third number: ")
if(check(n1,n2,n3)):
    print(f"Numbers {n1}, {n2}, and {n3} are different")
else:
    print("Numbers are the same")

