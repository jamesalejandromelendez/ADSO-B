import random
tam=0
vec=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)  
cp, ci, sp, si = 0, 0, 0, 0
for i in range (len(vec)):
    if vec [i]%2==0:
        print (vec[i]," par")
        cp += 1
        sp +=vec[i]
    else:
        print(vec[i],"impar")
        ci += 1
        si +=vec[i]
print("pares",cp, "impares",ci)
print ("total de pares", sp,"totas de impares",si)
print("su promedio es", sp // cp)