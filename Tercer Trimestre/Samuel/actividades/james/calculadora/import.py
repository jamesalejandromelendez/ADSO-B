import modulos
m = int(input("1.) digita tu numero: "))
x = int(input("2.) digita tu numero: "))
o = input("que operacion desea realizar\nsuma= +\nresta= -\nmultiplicar= *\ndividir= /\n: ")
if o == "+":
    print(modulos.suma(m,x))
if o == "-":
    print(modulos.resta(m,x))
if o == "*":
    print(modulos.multiplicar(m,x))
if o == "/":
    print(modulos.dividir(m,x))