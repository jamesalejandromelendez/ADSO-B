import random
vec=[]
tam = 0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for x in range (len(vec)):
 while x <= vec:
    if vec % x == 0:
        y = y + 1
    x = x + 1 
 if y == 2:
    print("el numero ",vec, "es primo ")
 else:
    print("el numero ",vec, "no es primo")