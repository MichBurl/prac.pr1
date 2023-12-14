def f(dice):
    #lista=list(dice)
    liczby=[]
    ilosc=0
    for i in range(len(dice)):
        ilosc = dice.count(str(i))
        liczby.append(ilosc)
    for i in range(len(liczby)):
        if liczby[i]==max(liczby):
            return i     
    
print(f("2133"))