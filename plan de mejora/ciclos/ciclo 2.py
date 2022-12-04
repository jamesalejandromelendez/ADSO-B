
while True:
    horas=int(input("numero de horas: "))
    if horas == 0:
        break
    presio=int(input("que presio tiene la hora?  "))
    nombre=input("nombre: ")
    if horas <= 40:
        salario = horas * presio
        print("el salario de ",nombre, "es", salario)
    else:
        salario = 40 * presio + 1.5 * (horas-40)*presio
        print("el salario de ",nombre, "es", salario)
