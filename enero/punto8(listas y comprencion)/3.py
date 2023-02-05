import random
# crea una lista utilizando diferentes funciones para la misma
print('\nejercicio 3')
def insertar():
    numeros.append(round(random.random()*10))
    print(numeros)
def ordernar():
    numeros.sort()
    print(numeros)
def invertidos():
    numeros.reverse()
    print(numeros)
    
tam = int(input('numero: '))
numeros = [round(random.random()*5) for i in range(tam)]
print(numeros)
insertar()
ordernar()
invertidos()