def try_syntax(numerator, denominator):# declara una funcion llamada try_syntax con dos argumentos
    try:# entra a un bloque  de exepciones
        print(f'In the try block: {numerator}/{denominator}')# imprime un mensaje con lo aggumentos dados
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator#imprime la divicion de los argumentos dados
    except ZeroDivisionError as zde:#en caso de que en codigo entre en error por divicion 
        print(zde)# imprime el mensaje en caso de que la exepcion sea cierta 
    else:#
        print('The result is:', result)#imprime el mensaje  dado mas el resultado
        return result#retorna el resultado del argumento
    finally:
        print('Exiting')#imprime el mensaje exiting
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 'a'))#comienza a operar la funcion y inserta los argumentos a operar