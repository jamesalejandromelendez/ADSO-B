class Metodo_Pago():

    def __init__(self, nom):
        self.nombre= nom

    def __str__(self):
        txt = "Pago: {0}"
        return txt.format(self.nombre)
    
class Cliente():

    def __init__(self, nom, edad):
        self.nombre=nom
        self.edad=edad
        self.pago=[]

    def __str__(self, MetodoPago):
        self.pago.append(MetodoPago)
        txt="Cliente: {0} - de {1} años, paga con: ({2})"
        return txt.format(self.nombre, self.edad, self.Metodo)



pagos1 = Metodo_Pago("Efectivo")
pagos2 = Metodo_Pago("Credito")
pagos3 = Metodo_Pago("Debito")


Cliente1=Cliente("Carlos", 18, pagos3)
print(Cliente1)