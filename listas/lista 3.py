import random
tam=0
vec=[int(random.random()*100) for i in range(10,25)]
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
print("pares",cp,"su suma total es ",sp,"impares",ci,"su suma total es ",si)
print("su promedio es", sp // cp)