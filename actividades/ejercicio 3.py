import random
tam=random.randint(10,25)
lis = []
suma = 0
media = 0 
vmi = 0
vma = 0
for i in range (tam):
    lis.insert(0,random.randint(0,100))
for i in range (len(lis)):
    if lis != 0:
         suma += lis[i]
         media = suma // tam
         vmi = min(lis)
         vma = max(lis)
swapped = True  

while swapped:
    swapped = False  
    for i in range(len(lis) - 1):
        if lis[i] > lis[i + 1]:
            swapped = True  
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
print(lis)
print("la suma de sus digitos es ", suma)
print("la media de sus digitos es ", media)
print(lis)
    
