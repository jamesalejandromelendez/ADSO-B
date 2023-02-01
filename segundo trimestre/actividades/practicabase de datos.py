my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = int(input("su numero es  "))
if val in my_list:
    print ("su numero si esta en nuesta lista")
else:
    print ("su numero no esta en el sistema, desea agregarlo?")
    res = input("responde con un si o un no ")
    if res == "si":
            my_list.append(val)
            print (my_list)
            print ("su numero a sido agregado exitosamente")