hora = int(input("que hora es "))
minutos = int(input("que minuto es "))
segundos = int(input("que segundo es "))
segundos = segundos + 1
if segundos >= 60:
    segundos = 0
    minutos = minutos +1
if minutos >= 60:
    minutos = 0
    hora = hora + 1
if hora > 23:
    hora = 0
print (hora, minutos, segundos, sep=":")




