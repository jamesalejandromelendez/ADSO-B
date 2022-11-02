import random
tam, prom = 0, 0
vec=[]
suma = 0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
s = True  

while s:
    s = False  
    for i in range(len(vec) - 1):
        if vec[i] > vec[i + 1]:
            s = True  
            vec[i], vec[i + 1] = vec[i + 1], vec[i]
print (vec)

