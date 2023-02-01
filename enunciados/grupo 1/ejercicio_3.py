"""crear un programa que le pida al usuario la edad
y los ingresos mensuales, determinar si debe pagar 
impuesos, pagara impuestos si es mayor de 16 años y
 ganar mas de 1000 euros"""
e = int(input("su edad es: "))
if e <= 16:
    print("no debes impuestos ")
else:
    i = int(input("monto de ingresos al mes: "))
    if i >= 1000:
        print("debes impuestos ")
