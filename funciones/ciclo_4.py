def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("introduzca un numero:"))
 
if NumeroPerfecto(num):
  print("%s es un numero perfecto" % num)
else:
  print("%s NO es un numero perfecto" % num)
  
  num = int(input()) #aquí se lee el número entero
contador = 0
print("los divisores de ",num)
for divisor in range(1,num+1):
    if (num % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",num," tiene ",contador," divisores")