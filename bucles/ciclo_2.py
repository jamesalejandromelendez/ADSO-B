def primo (num):
    x = 1
    y = 0
    while x <= num:
        if num % x == 0:
            y += 1
        x += 1
    if y == 2:
        return"el numero ",num, "es primo"
    else:
        return"el numero ",num, "no es primo"

num = int(input("ingresa tu numero "))
print(primo(num))
