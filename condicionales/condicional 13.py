j=int(input("ingrese cantidad de segundos:"))
horas=j//3600
sobrante1=j%3600  
minutos=sobrante1//60
sobrante2=sobrante1%60
print("horas", horas, "minutos", minutos, "segundos", sobrante2, sep=":")
