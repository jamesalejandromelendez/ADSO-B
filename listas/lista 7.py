import random
suma, prom = 0, 0
vec=[int(random.random()*100) for i in range(10,25)]
print(vec)
for i in range (len(vec)):
    if vec !=0:
        suma+=vec[i]
        prom = suma // len(vec)
print ("la suma de todos da: ",suma,"y el promedio es: ",prom)