"""numero de tres digitos donde la suma del cubo de cada digito sea igual al numero"""
for j in range (100, 1000):
    dg = 0
    suma = 0
    i = j 
    while i > 0:
        x =i % 10
        n = i // 10
        dg = x**3
        suma += dg
        i =n 
    if suma == j:
        print(j)