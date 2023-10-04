class motor():
    def __init__(self,cilindros,CF):
        self.cilindros = cilindros
        self.Cf = CF
        
    def __repr__(self):
        return f'el motor de {self.cilindros} cilindros tiene {self.Cf} CF'
    
    def trabaja(self,CF):
        for i in range(self,CF):
            print(i,end='')
            
class auto:
    def __init__(self,modelo,precio):
        self.modelo=modelo
        self.precio=precio
        self.motor=motor(4,100)
    
    def info(self):
        return f'el auto {self.modelo} con motor {self.motor} cueta {self.precio}'

    def emcender(self):
        print('enciende motor')
        self.motor.trabaja()
        
auto1=auto('Mazda 323',23000000)
auto1.emcender()