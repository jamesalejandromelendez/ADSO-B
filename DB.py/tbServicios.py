import sqlite3
with sqlite3.connect('D:\TechInn.db') as T:
    micursor=T.cursor()

class tbServicios:

    def __init__(self,nombre,documento):
        pass

    def buscar(coneccion, servID):
        micursor=coneccion.cursor()
        sentencia=f'Select * from tbServicios where servID={servID}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def modificar(coneccion, campo, valor, id):
        micursor=coneccion.cursor()
        sentencia=f'UPDATE tbServicios SET {campo}="{valor}" WHERE servID={id}'
        print(micursor.execute(sentencia).fetchall())
        sentencia=f'Select * from tbServicios where servID=12345'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def eliminar(coneccion,id):
        micursor=coneccion.cursor()
        sentencia=f'DELETE FROM tbServicios WHERE servID={id}'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

    def agregar(coneccion,servID,servDescripcion,servCosto,tiposerID):
        micursor=coneccion.cursor()
        sentencia=f'INSERT INTO tbServicios VALUES ({servID},"{servDescripcion}",{servCosto},{tiposerID})'
        print(sentencia)
        print(micursor.execute(sentencia).fetchall())

tbServicios.buscar(T,1)
# tbServicios.modificar(T,'servCosto', 38, 1)
# tbServicios.eliminar(T,1)
# tbServicios.agregar(T,1,'servicio de habitacion, reserva tu habitacion de acuerdo a tus nesecidades puedes escoger entre cama doble sencilla y matrimonial',38,1)