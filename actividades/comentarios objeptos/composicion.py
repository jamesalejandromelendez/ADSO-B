class Aprendiz:#se crea la clase aprendiz
    def __init__(self,nombre):#se crea el constructro de la clase con un parametro 'nombre'
        self.__nombre=nombre#se le asigna self.__titulo a la propiedad nombre
        self.__cursos=[]#se le asigna una lista a self.__cursos

    def agregarCurso(self,titulo):#se crea un metodo llamado 'agregar curso'
        self.__cursos.append(titulo)#se le agrega a self.__cursos el parametro titulo

    def getCursos(self):#se crea un metodo
        return self.__cursos#retorna los cursos agregados por self.__cursos

class Curso:#se crea una nueva clase llamada 'curso'
    def __init__(self,titulo):#se crea el constructro de la clase con un parametro 'titulo'
        self.__titulo=titulo#se le asigna self.__titulo a la propiedad titulo

    def getTitulo(self):#se define un nuevo metodo llamado 'gettitulo'
        return self.__titulo#retorna los datos guardados en el self.__ttulo 
    
a=Aprendiz('Martha')#se la agrega al objepto la clase aprendiz con el argumento martha
c1=Curso('Python Intermedio')#se le agrega al objepto 'c1' la clase aprendiz con un argumento 'python intermedio'
c2=Curso('Python Basico')#se le agrega al objepto 'c2' la clase aprendiz con un argumento 'python basico'
c3=Curso('Introduccion a Java')#se le agrega al objepto 'c3' la clase aprendiz con un argumento 'introduccion a java'

a.agregarCurso(c1)#se llama el metodo agregar curso con el objepto 'a' y como parametro trae a otro objepto 'c1' 
a.agregarCurso(c2)#se llama el metodo agregar curso con el objepto 'a' y como parametro trae a otro objepto 'c2' 
a.agregarCurso(c3)#se llama el metodo agregar curso con el objepto 'a' y como parametro trae a otro objepto 'c3' 

print(a.getCursos())#imprime los cursos guardados en el objepto 'a'


for curso in a.getCursos():#  la palabra curso entra a un recorrido por los cursos guardados por el objeto a
    print(curso.getTitulo())#imprime curso por curso que se encuentra en el objepto 