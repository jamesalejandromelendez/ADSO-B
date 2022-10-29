num = int(input("introduce tu numero  "))
for i in range (2, num + 1):
    if (num % i == 0):
        print(i, "es divisor de  ", num)