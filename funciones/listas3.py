''' 6. Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el 
usuario. Mínimo debe tener 5 elementos y máximo 20. '''

def fibonacci(cantidad):
    fibonacci = [0,1]
    for i in range(cantidad - 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
    
cantidad = int(input("Ingrese la cantidad de elementos que desea imprimir: "))
print("Serie de Fibonacci: ",fibonacci(cantidad))
"""este codigo no lo hice yo, lo hizo dionigi """ 