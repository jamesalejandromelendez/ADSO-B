values = (1, 0)#  es una variable que guarda dos valores enteros
#x,y=10,12
#print(divmod(10,3))
try:# entra a un bloque  de exepciones 
    q, r = divmod(*values) # son dos variables con la funcion de conciente y residuo 
    #print('valor de q=',q)
    print(f'q={q}')#imprime el resultado del conciente
    print(f'r={r}')#imprime el resultado del residuo 
except (ZeroDivisionError, TypeError) as e: #entra en ejecucion en caso tal de que el codigo caiga en error de divicion por cero o tipo de error 
    print(type(e), e)