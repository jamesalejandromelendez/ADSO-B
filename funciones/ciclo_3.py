num = int(input("ingrese su numero "))
i = 1
total = 0
while (i<num):
    if num%i == 0:
        total=total+i
    i=i+1
if total==num:
    print("el numero es perfecto ")
else:
    print(" el numero no esperfecto")
