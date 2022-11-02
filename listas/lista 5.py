"""import random
tam, pos = 0, 0
vec=[]
usu = []
cant = []
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
cont = 0
usu = int(input("ingresa tu numero "))
for i in range (len(vec)):
    cont=0
    for j in vec:
        if usu == j:
            cont+=1
    if cont!=0:
        cant.append(cont)
        pos = (len(vec))
    else:
        vec.append(usu)
print (cant[-10])
print(vec)
print (pos)"""
operacion = (input("que operacion desea hacer "))
x = int(input("digite su nimero"))
y = int(input())
c = 0 
if operacion == "%":
    c = x // y
print("su resultado es ",c)