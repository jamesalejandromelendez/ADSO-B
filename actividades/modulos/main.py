import sys
from sys import path


for i in sys.path:
    print(i)


print(path.append('..\\instructor samuel 2 - copia'))
#C:\Users\james\Desktop\instructor samuel 2 - copia\paquete
import james.tienda.operaciones as g
productos = {'cafe':3000,'jabon':10000,'lapiz':1000}
print(g.agregar(productos))
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
#print(modulo.suml(zeroes))
#print(modulo.prodl(ones))