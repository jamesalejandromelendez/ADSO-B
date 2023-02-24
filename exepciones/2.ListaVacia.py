lista = []

def error2(l):
    return l[0]

try:
    print(error2(lista))
except IndexError:
    print('La lista no puede estar vacía')
except:
    print('Error')