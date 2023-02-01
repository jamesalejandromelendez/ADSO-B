import datetime
año = int(input("inserte un año"))
mes = int(input("inserte un mes"))
dia = int(input("inserte un dia"))
fecha = datetime.datetime(año, mes, dia)
fecha_a = datetime.datetime.now()
diferecia = fecha - fecha_a  
dias_R = diferecia.days
if dias_R - 0:
    print("han pasado ",dias_R, "dias")
else:
    print("faltan ", dias_R)