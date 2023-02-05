"""crea una calcuradora basica"""
def suma ():
    if o == "+":
        r = m + x
    print("su resultado es: ",r)
def resta ():
    if o == "-":
        r = m - x
    print("su resultado es: ",r)
def multiplicar ():
    if o == "*":
        r = m * x
    print("su resultado es: ",r)
def dividir ():
    if o == "*":
        r = m * x
    print("su resultado es: ",r)

while True:
    m = int(input("1.) digita tu numero: "))
    if m == 0 or "":
        print("...")
        break
    x = int(input("2.) digita tu numero: "))
    if x == 0 or "":
        print("...")
        break
    o = input("que operacion desea realizar\nsuma= +\nresta= -\nmultiplicar= *\ndividir= /\n: ")
    if o == "":
        print("...")
        break
    if o == "+":
        suma()
    if o == "-":
        resta()
    if o == "*":
        multiplicar()
    if o == "/":
        dividir()