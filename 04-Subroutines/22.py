def f(number1,number2,number3):
    numbers=[number1,number2,number3]
    smallest=min(numbers)
    largest=max(numbers)
    return largest-smallest
print(f(2,12,8))