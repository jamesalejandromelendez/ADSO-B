def cifrado():
    codigo = ''
    for i in x:
        if i == 'X' or i == 'Y' or i == 'Z':
            z = ord(i)+9
            codigo += chr(z)
        elif i == 'x' or i == 'y' or i == 'z':
            z = ord(i)-55
            codigo += chr(z)
        else:
            z = ord(i)+3
            codigo += chr(z)
    print(codigo)
x = input('escribe una cadena: ') 
cifrado()