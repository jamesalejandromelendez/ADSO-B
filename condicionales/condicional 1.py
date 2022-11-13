x = int (input('digite el primer numero'))
y = int (input('digite el segundo numero'))
z = int (input('digite el tercer numero'))

menor = min(x,y,z)
mayor = max(x,y,z)
valor_medio = (x + y + z) - menor - mayor
print ("el valor medio es", valor_medio)
