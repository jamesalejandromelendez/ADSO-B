import random
tam = 0
vec=[]
x,y,z=0,1,0
while tam<5 or tam>20:
    tam = int(input("Ingresa un numero mayor a 5 y menor a 20   "))
vec.append(1)
for i in range(tam):
    z=x+y
    vec.append(z)
    x=y
    y=z
print(vec)