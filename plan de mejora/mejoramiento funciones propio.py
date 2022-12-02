"""Diseñar un procedimiento que acepte un número de
mes, un número de día y un número de año y los visualice en el formato
dd/mm/aa
 Por ejemplo, los valores 19,09,1987 se visualizarían
como
19/9/87
 y para los valores 3, 9 y 1905
3/9/05"""
def fecha ():
    D=int(input("ingrese el numero de dia "))
    while D<1 or D>31:
        print("por favor ingrese un dia dentro del rango segun el calendario ")
        D=int(input("ingrese el numero de dia "))
    M=int(input("ingrese el numero de mes "))
    while D<1 or D>12:
        print("por favor ingrese un mes dentro del rango segun el calendario ")
        M=int(input("ingrese el numero de mes "))
    A=int(input("ingrese el año "))
    while A<1000:
        print("por favor ingrese un año no menor de 1000 ")
        A=int(input("ingrese el año "))
    print("su fecha es ")
    print(D, M, A, sep="/")

fecha()