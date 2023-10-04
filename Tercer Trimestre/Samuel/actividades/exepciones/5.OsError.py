#OSERROR
'''Esta excepción se produce cuando una función del sistema retorna un error relacionado 
con el sistema, que incluye fallas de E/S como file not found o disk full 
(no para tipos de argumentos ilegales u otros errores incidentales).'''

x='fichero.txt'

def SisopError(x):
    with open(x) as file:
        read_data = file.read()
    return read_data

try:
    SisopError(x)
except OSError:
    print('OSError. No se pudo abrir')
except:
    print('Todo salio mal')