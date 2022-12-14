"""Calcular la operación x n sin utilizar la función pow"""
n = int(input("numero base: "))
e = int(input("numero exponente: "))
s = 0
for i in range (e):
    total = n**e 
    s += total
print(total)
