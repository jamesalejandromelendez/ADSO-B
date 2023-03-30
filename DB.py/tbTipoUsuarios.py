import sqlite3
with sqlite3.connect('D:\TechInn.db') as T:
    micursor=T.cursor()

class tbTipoUsuario:

    def __init__(self,nombre,documento):
        pass

    def buscar( tipoUsuID):
        micursor= T.cursor()
        sentencia=f'Select * from tbTipoUsuario where tipoUsuID={tipoUsuID}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def modificar(tipoUsuID,valor):
        micursor= T.cursor()
        sentencia=f'UPDATE tbtipoUsuario SET tipoUsuRol="{valor}" WHERE tipoUsuID={tipoUsuID}'
        print(micursor.execute(sentencia).fetchall())
        sentencia=f'Select * from tbTipoUsuario where tipoUsuID=12345'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def eliminar(tipoUsuID):
        micursor= T.cursor()
        sentencia=f'DELETE FROM tbTipoUsuario WHERE tipoUsuID={tipoUsuID}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def agregar(tipoUsuID,tipoUsuRol):
        micursor= T.cursor()
        sentencia=f'INSERT INTO tbTipoUsuario VALUES ({tipoUsuID},"{tipoUsuRol}")'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

# tbTipoUsuario.buscar(T,1)
# tbTipoUsuario.modificar(T,1,'Cliente')
# tbTipoUsuario.eliminar(T,1)
# tbTipoUsuario.agregar(T,1,'Cliente')