#IOError en Python es el resultado de un nombre de archivo o ubicación incorrectos.
try:
   archivo = open("archivo.txt","r")
   contenido = archivo.read()
   archivo.close()
except IOError:
   print("No se pudo abrir el archivo")