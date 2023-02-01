import random

c, s, p = 0, 0, 0
vector=[int(random.random()*100)for i in range(10)]
tam=len(vector)
for i in range(tam):
    vector.insert(i,round(random.random()*100))
    c+=1
    s+=vector [i]
    p = s // c
print(vector)
for i in range (len(vector)):
    if vector[i]==p:
        print(vector[i],"el valor es igual al promedio")
    elif vector[i]>p:
        print(vector[i],"el valor es mayor que el promedio")
    elif vector[i]<p:
        print(vector[i],"el valor es menor que el promedio")
print ("el promedio es ",p)