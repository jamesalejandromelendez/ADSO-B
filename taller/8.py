def cifrado():
    abecedario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codigo = []
    for i in x:
        if i in abecedario:
            z = abecedario.index(i)
            c = abecedario[z+3]
            codigo.append(c)
    print(codigo)
x = input('escribe una cadena: ') 
cifrado()