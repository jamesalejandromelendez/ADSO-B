def materias():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    aprovadas = []
    for i in materias:
        score = float(input("¿Qué nota has sacado en " + i + "?"))
        if score >= 5:
            aprovadas.append(i)
    for i in aprovadas:
        materias.remove(i)
    print("Tienes que repetir ", str(materias))


materias()