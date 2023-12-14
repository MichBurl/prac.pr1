def f(name):
    acr=name.split(' ')
    for i in range(len(acr)):
        print(acr[i][0], end='')
f("For Your Information")