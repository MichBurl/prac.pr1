def f(n):
    if n==1: return "*"
    else:
        for i in range(n):
            print("*", end='')
            if i!=n-1: print("/", end='')
f(4)