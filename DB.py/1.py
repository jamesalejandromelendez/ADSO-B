import sqlite3
with sqlite3.connect('D:\TechInn.db') as T:
    #Cursor=T.cursor()
    micursor=T.cursor()
    #sentencia='UPDATE tbUsuarios SET usuNombre="james" WHERE usuDocumento=12345'
    #print(micursor.execute(sentencia).fetchall())
    #sentencia='Select * from tbUsuarios where usuDocumento=12345'
    #print(T.execute(sentencia).fetchall())

# def busqueda(coneccion, documento):
#     micursor=coneccion.cursor()
#     sentencia=f'Select * from tbUsuarios where usuDocumento={documento}'
#     print(sentencia)
#     print(micursor.execute(sentencia).fetchall())

def modificar(coneccion,tabla, campo, valor, id):
    micursor=coneccion.cursor()
    sentencia=f'UPDATE {tabla} SET {campo}="{valor}" WHERE usuDocumento={id}'
    print(micursor.execute(sentencia).fetchall())
    sentencia=f'Select * from tbUsuarios where usuDocumento=12345'
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

def eliminar(coneccion,campo,dato,id):
    micursor=coneccion.cursor()
    sentencia=f'DELETE tbUsuarios SET {campo}={dato} WHERE usuDocumento={id}'
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

#busqueda(T,12345)
#modificar(T, 'tbUsuarios','usuNombre', 'james', 12345)
eliminar(T, 'usuGenero', '','1223567')


