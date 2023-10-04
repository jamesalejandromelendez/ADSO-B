class Curso:#se crea una clase llamada curso 
    def __init__(self,titulo):#se crea el constructro de la clase con un parametro 'titulo'
        self.__titulo=titulo#se le asigna self.__titulo a la propiedad titulo

    def getTitulo(self):#se crea un metodo  llamado 'titulo'
        return self.__titulo#retorna la propiedad titulo

class Aprendiz:#se crea la clase aprendiz 
    def __init__(self,nombre):#se crea el constructro de la clase con dos parametros como 'nombre' y self
        self.__nombre=nombre#se le asigna self.__nombre a la propiedad nombre
        self.__cursos=[]#se le asigna self.__cursos una lista

    def agregarCurso(self,nombreCursito):#se define un metodo  llamado agregar curso con dos parametros, 'nombre' y self
        cursito=Curso(nombreCursito)#en esta linea se define la variable cursito con  el argumento dado por la funcion
        self.__cursos.append(cursito)# se le asigna el parametro curso al self.__curso

    def getCursos(self):#se define un metodo llamado cursoso 
        return self.__cursos#retorna self.__cursos donde se encuentra los cursos guardados anteriormente 
    
ap=Aprendiz('Sofia')#se le asigna al objepto ap la clase aprendiz con el parametro 'sofia'
ap.agregarCurso('Python Basico')#se le agrega el parametro 'python basico' al metodo agregarcurso
ap.agregarCurso('Python Intermedio')#se le agrega el parametro 'pytohn intermedio' al metodo agregarcurso

for c in ap.getCursos():# c toma cada uno de los cursos almacenados en el metodo getcursos
    print(c.getTitulo())#imprime el curso tomado por c