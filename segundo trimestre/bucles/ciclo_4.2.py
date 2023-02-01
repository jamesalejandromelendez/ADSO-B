for n in range (1,1001):
    suma = 0
    for i in range (1,n):
        if n % i == 0:
            print("divisor", i)
            suma = suma + 1
        if suma == n:
            print ("perfecto", i) 
