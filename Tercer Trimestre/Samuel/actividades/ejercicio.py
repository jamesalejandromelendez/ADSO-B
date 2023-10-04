class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.__cont=0
        self.__nombre=nombre 
        self.__cargo=cargo 
        self.__salario=salario
        print('numero de veces',self.__cont)
        
    def setinformacion(self,nombre,cargo,salario ):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        
    def hora(self):
        p=self.__salario//240
        print(f'el costo de su hora es {p}')
        
    def imcremento(self):
        if self.__salario == 1160000:
            i=(self.__salario*16.3)//100
            return 'su salario mas el incremento de ipc es: ',i+self.__salario
        else:
            a=(self.__salario*13.3)//100
            return 'su salario mas el incremento de ipc es: ',a+self.__salario
        
    def extras(self):
        x=int(input('horas extras: '))
        if x<40:
            z= self.__salario//240
            print(f'su salario mas horas extras es: {z*x+self.__salario}')
        else:
            return 'no se puede realizar mas de dos horas diarias'
    
    def sucecion(self):
        self.__cont+=1        
    def getdatos(self):
        return self.__nombre, self.__cargo, self.__salario
            
empleado = Empleado('james','gerente',1160000)
print(empleado.hora())
print(empleado.imcremento())
print(empleado.getdatos())
print(empleado.extras())
empleado.sucecion()

trabajador = Empleado('diego','supervisor',1170000)
print(trabajador.hora())
print(trabajador.imcremento())
print(trabajador.getdatos())
print(trabajador.extras())
trabajador.sucecion()
