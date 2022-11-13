import random
vecprimos=[]
vec=[int(random.random()*100) for i in range(10,25)]
print(vec)
for x in range (len(vec)):
    contar=0
    y=1
    while y <=vec[x]:
        if vec[x] % y == 0:
            contar+=1
        y+=1
    if contar == 2:
        vecprimos.append(vec[x])
print("los números primos son:",len(vecprimos),"y son:",vecprimos)