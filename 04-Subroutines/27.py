def f(text):
    lista=list(text)
    for i in range(len(lista)):
        if i == len(lista)-1:
            print(lista[i])
        else:
            print(lista[i], end='-')

f("University")