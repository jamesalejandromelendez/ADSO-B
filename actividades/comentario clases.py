class Persona:#crea una clase llamada persona
    def __init__(self,nombre):#crea un constructor 
        self.__nombre=nombre#guarda en el parametro dado por el usuario
        print('Activando constructor')#imprime en pantalla 'activando constructor'

    def getNombre(self):#crea una funcion o metodo dentro de la clase persona
        return self.__nombre#retorna el nombre que se le fue dado al objeto
    
    def setNombre(self, nombre):#crea una funcion o metodo para la clase persona con un argumento con el nombre: 'nombre'
        self.__nombre=nombre#coloca o actualiza el parametro dado por el usuario en __nombre

    def metodo(self):#crea una funcion o un metodo 
        print('Soy un método')#imprime un mensaje 'soy un metodo'

ob=Persona('Ana')#se le asigna al objeto 'ob' la clase persona
print(ob.getNombre())#imprime y llama la funcion de la clase presona 'getnombre'
ob.setNombre('Maria')#llama la funcion de la clase 'setnombre'
print(ob.getNombre())#se le asigna al objeto 'getnombre' la clase persona
#ob.metodo()
#print(type(ob))