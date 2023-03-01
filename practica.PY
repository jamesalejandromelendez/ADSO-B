class persona :
    def __init__(self,nombre):
        self.__nombre=nombre
    def setdocumento(self,documento):
        self.__documento=documento
    def settelefono(self,telefono):
        self.__telefono=telefono
    def getinforme(self):
        return self.__nombre, self.__telefono, self.__documento
    
estudiante=persona(input('cual es tu nombre'))
print(estudiante.setdocumento(input('cual es tu documento: ')))
print(estudiante.settelefono(input('cual es tu telefono: ')))
print(estudiante.getinforme())
