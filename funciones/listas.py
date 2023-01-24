import random
def llenarLista(list):
    r=round(random.randint(5,20))
    for i in range(r):
        list.append(round(random.randrange(100)))
    return list
def sumarLista(list):
    sma=0
    for i in list:
        sma+=i
    return sma
lista=[]
lista=llenarLista(lista)
print("la lista llena:",llenarLista(lista))
print("la suma de la lista es=",sumarLista(lista))
"""este codigo no lo hice yo, lo hizo joel oliveros"""
