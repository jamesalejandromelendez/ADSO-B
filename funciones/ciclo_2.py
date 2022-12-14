num = int(input("ingresa tu numero"))
x = 1
y = 0
while x <= num:
    if num % x == 0:
        y = y + 1
    x = x + 1
if y == 2:
    print("el numero ",num, "es primo ")
else:
    print("el numero ",num, "no es primo")