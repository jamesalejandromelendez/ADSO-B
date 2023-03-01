def edad():#declara la funcion llamada edad
    try:#inicia un bloque de exepciones
        tuedad=int(input("introduce tu edad"))#el usuario inserta un caracter a la variable 
        print(f'tu edad es  {tuedad}')#imprime en pantalla el mensaje tu edad y muestra el caracter agregado por el usuario
        #print('Tu edad es ',tuedad)
    except ValueError as e: #en caso de que el usuario ingrese un caracter no numerico entra a operar la exepcion valueerror renombrada como e
        print(e)#imprime el tipo de error en pantalla
        print("La edad debe ser un valor numerico...")#imprime en mesaje La edad debe ser un valor numerico... en pantalla
        edad()#vuelve a llamar la funcion 
    
edad()#llama la funcion a operar