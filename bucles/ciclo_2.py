def primo (num):
    x = 1
    y = 0
    while x <= num:
        if num % x == 0:
            y += 1
        x += 1
    if y == 2:
        print("el numero ",num, "es primo")
    else:
        print("el numero ",num, "no es primo")

num = int(input("ingresa tu numero "))
primo(num)