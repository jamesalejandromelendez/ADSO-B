#http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-decision-python.html

"""6. Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, 
imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. 
Si no es así, imprimir “no hay coincidencia”."""

def comparacion (nombre1,nombre2):
    final=len(nombre1)-1
    final2=len(nombre2)-1
    if nombre1[0] == nombre2[0]:
        print("hay coincidencia coincidencia en la primera letra")
    elif nombre1[final] == nombre2[final2]:
        print("hay conicidencia en la ultima letra")
    else:
        print("no hay coincidencia")    
nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
comparacion(nombre1,nombre2)