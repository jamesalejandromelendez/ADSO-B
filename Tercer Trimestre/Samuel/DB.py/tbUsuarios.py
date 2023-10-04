import sqlite3
with sqlite3.connect('D:\TechInn.db') as T:
    micursor=T.cursor()

class tbUsuarios:

    def __init__(self,nombre,documento):
        pass

    def buscar( documento):
        micursor=T.cursor()
        sentencia=f'Select * from tbUsuarios where usuDocumento={documento}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def modificar( campo, valor, id):
        micursor=T.cursor()
        sentencia=f'UPDATE tbUsuarios SET {campo}="{valor}" WHERE usuDocumento={id}'
        print(micursor.execute(sentencia).fetchall())
        sentencia=f'Select * from tbUsuarios where usuDocumento=12345'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def eliminar(id):
        micursor=T.cursor()
        sentencia=f'DELETE FROM tbUsuarios WHERE usuDocumento={id}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def agregar(documento,nombre,apellido,email,telefono,genero,tipo):
        micursor=T.cursor()
        sentencia=f'INSERT INTO tbUsuarios VALUES ({documento},"{nombre}","{apellido}","{email}",{telefono},"{genero}",{tipo})'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

# tbUsuarios.buscar(T,123)
# tbUsuarios.modificar(T, 'tbUsuarios','usuNombre', 'james', 12345)
# tbUsuarios.eliminar(T,1234567)
# tbUsuarios.agregar(T,1234,'andrea','vasques','andreavasquezgmailcom',30583849,'Femenino',2)

