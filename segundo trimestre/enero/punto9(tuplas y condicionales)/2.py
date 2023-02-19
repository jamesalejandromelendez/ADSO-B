"""Utiliza los símbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la 
siguiente tupla en una variable llamada operacion."""
print('\nejercicio 2')
def tupla():
    operacion = 0
    for i in numeros:
        if i != 1:
            operacion += i
        else:
            operacion -=1
    print(operacion,'\n')

numeros = (10, 1, 5, 11)
tupla()

