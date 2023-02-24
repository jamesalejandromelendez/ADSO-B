def error3():
    x = input('Ingrese nombre: ')
    b = input('Ingrese apellido: ')
    return x + b

try:
    print(error3())
except KeyboardInterrupt:
    print('Ups')
except:
    print('Error')