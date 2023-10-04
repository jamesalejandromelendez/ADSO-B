class registrar:
    registroA= {'123456': {'nombre': 'james', 'edad': '18', 'telefono': '305', 'contraseña': '321','curso':''}}
    registroI= {'123': {'nombre': 'samuel', 'edad': '38', 'telefono': '305', 'contraseña': '321','curso':''}}
    def __init__(self, i,documento, nombre, edad, telefono, contraseña):
        self.documento=documento
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.contraseña=contraseña

    def agregarA(self):
        registro = {'nombre':self.nombre, 'edad':self.edad, 'telefono':self.telefono, 'contraseña':self.contraseña}
        if self.documento not in registrar.registroA:
            registrar.registroA[self.documento] = (registro)
        print(registrar.registroA)

    def agregarI(self):
        registro = {'nombre':self.nombre, 'edad':self.edad, 'telefono':self.telefono, 'contraseña':self.contraseña}
        if self.documento not in registrar.registroI:
            registrar.registroI[self.documento] = (registro)
        print(registrar.registroI)

    def actualizarA(self,documento, nombre, edad, telefono, contraseña):
        registro = {'nombre':nombre, 'edad':edad, 'telefono':telefono, 'contraseña':contraseña}
        if documento in registrar.registroA:
            registrar.registroA[self.documento] = (registro)
        print(registrar.registroA)

    def actualizarI(self,documento, nombre, edad, telefono, contraseña):
        registro = {'nombre':nombre, 'edad':edad, 'telefono':telefono, 'contraseña':contraseña}
        if documento in registrar.registroI:
            registrar.registroI[self.documento] = (registro)
        print(registrar.registroI)

class estudiante(registrar):
    def __init__(self,identificacion,documento, nombre, edad, telefono, contraseña):
        super().__init__( identificacion,documento, nombre, edad, telefono, contraseña)

    def agregarA(self):
        return super().agregarA()

    def actualizarA(self,documento, nombre, edad, telefono, contraseña):
        return super().actualizarA(documento, nombre, edad, telefono, contraseña)

    def curso(self):
        x='123456' #input("id del estudiante: ")
        for i,a in registrar.registro.items():
            for r,t in curso.curso.items():
                if r == s:
                    curso={'curso':curso.curso[r]}
                    registrar.actualizarA[x] += (curso)
                    print('felicidades',a['nombre'], 'entraste al curso ',t['nombre']) 

class inscripcion(estudiante):
    def __init__(self, identificacion, documento, nombre, edad, telefono, contraseña):
        pass

class curso:
    curso={1:{'nombre':'ADSO','descripcion':'jsjsjs','año':'2'},
            2:{'nombre':'ADSI','descripcion':'jsjsjs','año':'1.5'},
            3:{'nombre':'ADMINISTRACION','descripcion':'jsjsjs','año':'1'},
            4:{'nombre':'CONSTRUCCION','descripcion':'jsjsjs','año':'1'}}
    def __init__(self):
        pass

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
        x = int(input('materia: '))
        z = input('programacion: ')
        materia[x]['cronograma'] = (z)
        print(materia[x]['cronograma'])

while True:
    x=input('presiona\n 1-registarse\n 2-iniciar sesion\n 0-salir\n')
    if x == '1':
        c=input('presiona\n 1-aprendiz\n 2-instructor')
        if c == '':
            break
        if c == '1':
            d=input('digite su numero de documento: ')
            n=input('digite su nombre: ')
            a=input('digite cuantos años tiene: ')
            t=input('digite su numero telefonico: ')
            c=input('crea una contraseña: ')
            aprendiz=estudiante('self',d,n,a,t,c)
            aprendiz.agregarA()
            print('ya puedes iniciar sesion')

        else:
            z=input('contraseña: ')
            if z == 'instructor1':
                d=input('digite su numero de documento: ')
                n=input('digite su nombre: ')
                a=input('digite cuantos años tiene: ')
                t=input('digite su numero telefonico: ')
                c=input('crea una contraseña: ')
                instructor=instructor('self',d,n,a,t,c)
                instructor.agregarI()
                print('ya puedes iniciar seccion')
    elif x == '2':
        d=input('numero de documento: ')
        if d in registrar.registroA:
            c=input('contraseña: ')
            for i,a in registrar.registroA.items():
                if c == a['contraseña']:
                    print('eres estudiante')
                    x=input('presiona\n 1-agregar curso\n 2-para actualizar datos\n')
                    if x == '1':
                        s=int(input('codigo de curso: '))
                        if s in curso.curso:
                            for r,t in curso.curso.items():
                                if r == s:
                                    registrar.registroA[i]['curso'] = (curso.curso[r])
                                    print('felicidades',a['nombre'], 'entraste al curso ',t['nombre'])
                                    print(registrar.registroA[i])

                    elif x == '2':
                        n=input('digite su nombre: ')
                        a=input('digite cuantos años tiene: ')
                        t=input('digite su numero telefonico: ')
                        c=input('crea una contraseña: ')
                        aprendiz=estudiante('self',d,n,a,t,c)
                        aprendiz.actualizarA(d,n,a,t,c)
                else:
                    print('intenta de nuevo')

        elif d in registrar.registroI:
            c=input('contraseña: ')
            for i,a in registrar.registroI.items():
                if c == a['contraseña']:
                    print('eres instructor')
                    x=input('presiona\n 1-agregar asignatura\n 2-para actualizar asignaruras\n 3-para actualizar datos')
                    if x == '2':
                        materia.programacion('self')
                    elif x == '3':
                        n=input('digite su nombre: ')
                        a=input('digite cuantos años tiene: ')
                        t=input('digite su numero telefonico: ')
                        c=input('crea una contraseña: ')
                        aprendiz=instructor('self',d,n,a,t,c)
                        aprendiz.actualizarI(d,n,a,t,c)
        else:
            print('debes crear un usuario primero')
    elif x=='0':
        break
    else:
        print('selecciona una opcion valida')