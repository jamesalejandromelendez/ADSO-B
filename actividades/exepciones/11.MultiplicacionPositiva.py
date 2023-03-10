def multiplicacion(a,b):
   resultado = a * b
   assert resultado >= 0, "El resultado de la multiplicación debe ser positivo"
   return resultado

print(multiplicacion(2,3))
print(multiplicacion(-2,3))