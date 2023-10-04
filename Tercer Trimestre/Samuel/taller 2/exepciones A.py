
try: #inicia un bloque de codigo de exepciones 
    #print(1/1))
    raise SyntaxError # sirve   
except SyntaxError as e: # Este exept corrije el error en caso tal de que tenga un error de sintaxis  
    print(e)#muestra o imprime el tipo de error 
    print('Cierra el parentesis')# imprime un mensaje en la cual le da una recomendacion
    
try:#inicia un bloque de codigo de exepciones 
    #raise ZeroDivisionError
    print(1/0)# imprime una divicion por cero a lo que arrojara un  error
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:# este except corrige el error del anterior print
    print(zde)# muestra o imprime el tipo de error 
    #print('prueba error')
