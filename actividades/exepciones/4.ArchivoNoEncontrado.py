#FileNotFoundError
'''El error FileNotFoundError: [Errno 2] No such file or directory, es un error común que lanza la librería OS. 
En esencia este error indica que estámos intentando acceder a un archivo o carpeta que no existe, 
ya sea porque no está presente en la ruta de archivo en particular o porque se ha cambiado su nombre.'''

#open("database.sqlite")

x="database.sqlite"
def abrirArchivo(x):
    open(x)
    return open
    
try:
    abrirArchivo(x)
except FileNotFoundError:
    print('Archivo no existe')
except:
    print('Todo salio mal')