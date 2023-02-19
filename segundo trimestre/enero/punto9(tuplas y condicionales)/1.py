#https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-de-listas-tuplas-y-diccionarios-en-python/
"""Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud 
máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa 
termina cuando el usuario introduce un cero."""
def contenido():
    while True:
        numero = int(input("Dame un numero entero: "))
        if numero==0:
            break
        else:
            if numero>=1 and numero<=len(meses):
                print(meses[numero-1])
            else:
                print("Inserta un numero entre 1 y ",len(meses))

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print('oprime el numero 0 para salir ')
contenido()



