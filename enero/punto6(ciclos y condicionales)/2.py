"""escribe un codigo para hacer un temporizador"""
def tem():
    for horas in range (0, 13,1):
        if horas == h:
            break
        for minutos in range (0, 60, 1):
            if minutos == m:
                break
            for segundos in range (0, 60, 1):
                if segundos == s:
                    break
                print (horas, minutos, segundos, sep=":")

h = int(input("hora: "))
m = int(input("minuto: "))
s = int(input("segundo: "))
tem()