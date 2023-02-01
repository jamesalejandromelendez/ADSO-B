import random
vec=[int(random.random()*100) for i in range(10,25)]
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