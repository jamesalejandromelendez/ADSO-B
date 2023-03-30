from tbUsuarios import *
from tbServicios import *
from tbTipoUsuarios import *
from tbReserva import *


print('BIENVENIDOS A NUESTRO HOTEL SENA TECH INN')
x=input('1-Usuario\n2-Administrador')
if x=='1':
    z=input('1-iniciar sesion\n2-registrarse')
    if z=='1':
        D=int(input('ingresa tu numero de documento'))
        tbUsuarios.buscar(D)
    pass
