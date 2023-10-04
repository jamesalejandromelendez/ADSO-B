import sqlite3
with sqlite3.connect('D:\TechInn.db') as T:
    micursor=T.cursor()

class tbReserva:

    def __init__(self,nombre,documento):
        pass

    def buscar(coneccion, resID):
        micursor=coneccion.cursor()
        sentencia=f'Select * from tbReserva where resID={resID}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def modificar(coneccion, campo, valor, id):
        micursor=coneccion.cursor()
        sentencia=f'UPDATE tbReserva SET {campo}="{valor}" WHERE resID={id}'
        print(micursor.execute(sentencia).fetchall())
        sentencia=f'Select * from tbReserva where resID=12345'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def eliminar(coneccion,id):
        micursor=coneccion.cursor()
        sentencia=f'DELETE FROM tbReserva WHERE resID={id}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def agregar(coneccion,resID,resCantPersonas,resFechaIn,resFechaSa,habID):
        micursor=coneccion.cursor()
        sentencia=f'INSERT INTO tbReserva VALUES ({resID},"{resCantPersonas}","{resFechaIn}","{resFechaSa}",{habID})'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

tbReserva.buscar(T,1)
# tbReserva.modificar(T, 'resCantPersonas',3,7)
# tbReserva.eliminar(T,7)
# tbReserva.agregar(T,7,3,'9-02-2023','20-02-2023',2)