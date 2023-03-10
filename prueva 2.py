# Probando propiedades: variables de instancia.
class Super:
    def __init__(self, i,documento, nombre, edad, telefono, contraseña):
        self.i=i
        self.documento=documento
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.contraseña=contraseña
        self.registro= {}
        
    def agregar(self):
        registro = {'nombre':self.nombre, 'edad':self.edad, 'telefono':self.telefono, 'contraseña':self.contraseña}
        if self.documento not in self.registro:
            self.registro[self.documento] = (registro)
        return self.registro

class Sub(Super):
    def __init__(self,identificacion,documento, nombre, edad, telefono, contraseña):
        super().__init__(identificacion,documento, nombre, edad, telefono,contraseña)
        #self.subVar = 12
        
obj = Sub('self','123456','james','18','306','321')
#print(obj.subVar)
print(obj.agregar())

