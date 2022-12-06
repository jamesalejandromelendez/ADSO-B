from random import randint
def positivos():
    suma3,suma4=0,0
    for i in (lista[0]):
        if i > 0:
            suma3 += i
    for i in (lista[1]):
        if i > 0:
            suma4+=i
    print("la suma de los positivos es: ",suma3 + suma4)

def negativos():
    suma1,suma2=0,0
    for i in (lista[0]):
        if i < 0:
            suma1 += i
    for i in (lista[1]):
        if i < 0:
            suma2 += i
    print("la suma de negativos es: ",suma1 + suma2)
    
lista=[]
for i in range(2):
    row = [(randint(-10,10)) for i in range(2)]
    lista.append(row)
print(lista)
positivos()
negativos()
