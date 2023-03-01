def repetidas(x):
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    repetidas =[]
    c = 0
    for i in x:
        if i in a:
            if i not in repetidas:
                c+=1
                repetidas.append(i)
    print('el total de letras es ',c,'\n',repetidas)
x = input('digita tu frace: ')
repetidas()