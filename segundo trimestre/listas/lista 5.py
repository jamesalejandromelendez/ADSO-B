import random
tam, pos, cont = 0, 0, 0
vec=[]
usu = []
cant = []
vec=[int(random.random()*100) for i in range(10,25)]
print(vec)
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
print (pos)