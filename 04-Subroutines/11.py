def f(x,y):
    amount=0
    for i in range(x,y):
        if(i%2==0 and i<0):
            amount+=1
    return amount
print(f(-7,8))

