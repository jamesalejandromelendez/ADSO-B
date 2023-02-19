x = input("Ingrese una palabra: ")
tilde =[]
for i in x:
        if i in "àèìòù":
            tilde.append(i)
if x[-1] in "àèìòù" or x[-2] in "àèìòù":
    print('aguda')
else:
    print(tilde[:])
    print('grave',tilde[-1])


        



