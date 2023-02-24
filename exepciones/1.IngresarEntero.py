def error1():
    variable = int(input('Ingresa un número: '))
    return variable * 10

try:
    print(error1())
except ValueError:
    print('Debe ingresar un número')
except:
    print('Error')