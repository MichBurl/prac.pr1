def f(x,y):
    lista=[]
    for i in range(x,y+1):
        if(i%2==0 and i%3==0 and i%4!=0):
            lista.append(i)
        else: continue
    print(lista)
    return sum(lista)
        
print(f(10,30))

