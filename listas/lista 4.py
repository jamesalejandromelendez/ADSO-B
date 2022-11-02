import random
tam=0
vec=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range(len(vec) - 1):
    if vec[i] > vec[i + 1]:
        vec[i], vec[i + 1] = vec[i + 1], vec[i]
        vec = vec
swapped = True
while swapped:
    swapped = False 
    for i in range(len(vec) - 1):
        if vec[i] > vec[i + 1]:
            swapped = True
            vec[i], vec[i + 1] = vec[i + 1], vec[i]
print(vec)