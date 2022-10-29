trabajo = int(input("cuantas horas trabajo?"))
pago_1 = trabajo * 2600
pago_2 = (trabajo - 40)*5000
if trabajo <= 40:
    print ("Su saldo sin extras es", pago_1 )
else:
    print ("su saldo con extras es de ", pago_2 + 104000)
