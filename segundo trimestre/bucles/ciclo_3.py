def perfecto (num):
    i = 1
    total = 0
    while (i<num):
        if num%i == 0:
            total=total+i
        i=i+1
    if total==num:
        return("el numero es perfecto ")
    else:
        return(" el numero no esperfecto")

num = int(input("ingrese su numero "))
print(perfecto(num))

