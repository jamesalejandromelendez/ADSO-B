class A1:#se crea una clase llamada 'a1' 
    def __init__(self):#se define el constructor 
        pass
    def saludo(self):#se define un metodo llamado 'saludo'
        print('Hola desde A1')#imprime en pantalla 'Hola desde A1'

class A2:#se crea una nueva clase llamada 'A2'
    def __init__(self):#se define el constructor
        pass
    def saludos(self):#se define un metodo llamado 'saludo'
        print('Hola desde A2')#imprime en pantalla 'Hola desde A2'


class B(A2,A1):#se crea una sudclase que como argumentos trae la clase 'A1' y 'A2'
    def __init__(self):#se define el constructor
        pass
    def saludoss(self):#se define un metodo llamado 'saludo'
        print('Hola desde B')#imprime en pantalla 'hola desde B'
    def __str__(self):#crea un metodo en str (este sirve para devolver una cadena anterior)
        return 'Soy un objeto de la clase B'#retorna el mensaje 'Soy un objeto de la clase B'
obj=B()#se le asigna al objeto la clase B
print(obj.__str__())#imprime el metodo de str del objeto 'obj'
obj.saludos()
obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())