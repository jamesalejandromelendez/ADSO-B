class registrar:
    registroI= {'123': {'nombre': 'samuel', 'edad': '38', 'telefono': '305', 'contraseña': '321','curso':''}}
    def __init__(self, i,documento, nombre, edad, telefono, contraseña):
        self.documento=documento
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.contraseña=contraseña

    def agregarI(self):
        registro = {'nombre':self.nombre, 'edad':self.edad, 'telefono':self.telefono, 'contraseña':self.contraseña}
        if self.documento not in registrar.registroI:
            registrar.registroI[self.documento] = (registro)
        print(registrar.registroI)

    def actualizarI(self,documento, nombre, edad, telefono, contraseña):
        registro = {'nombre':nombre, 'edad':edad, 'telefono':telefono, 'contraseña':contraseña}
        if documento in registrar.registroI:
            registrar.registroI[self.documento] = (registro)
        print(registrar.registroI)

class instructor(registrar):
    def __init__(self,identificacion,documento, nombre, edad, telefono, contraseña):
            super().__init__( identificacion,documento, nombre, edad, telefono, contraseña)
    def agregarI(self):
            return super().agregarI()

    def actualizarI(self,documento, nombre, edad, telefono, contraseña):
            return super().actualizarI(documento, nombre, edad, telefono, contraseña)

class materia(instructor):
    materia = {1:{'nombre':'matematicas','cronograma':'primer periodo'}}
    def __init__(self,id,nombre,cronograma):
         super().__init__(id,nombre,cronograma)
    def programacion(self):
        x = input('materia: ')
        z = input('programacion: ')
        materia[x]['cronograma'] = (z)
        print(materia[x]['cronograma'])
    


aprendiz=instructor('self','123456','james','18','305','321')
aprendiz.actualizarI('123456' ,'james','18','305','3212343456346')