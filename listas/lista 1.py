import random
tam=0
vec=[]
c, s, p = 0, 0, 0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
    c+=1
    s+=vec [i]
    p = s // c
print(vec)
for i in range (len(vec)):
    if vec[i]==p:
        print(vec[i],"el valor es igual al promedio")
    elif vec[i]>p:
        print(vec[i],"el valor es mayor que el promedio")
    elif vec[i]<p:
        print(vec[i],"el valor es menor que el promedio")
print ("el promedio es ",p)