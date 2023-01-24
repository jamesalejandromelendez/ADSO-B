def divisor(num):
    contador=0
    for i in range (2, num + 1):
        if (num % i == 0):
            contador+=i
    return "el numero ",num,"tiene ",contador,"divisores"
num = int(input("introduce tu numero  "))
print(divisor(num))