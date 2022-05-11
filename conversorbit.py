from collections import deque

class Conversorbit:
    def __init__(self ):
        self.resultado=0
        self.convertido = []
        self.lista = deque()
        self.hexaconvt=0

    def conver_to_Hex(self):
        return ('{:X}'). format(self.resultado)

    def convertBit(self):
        self.hexaconvt = self.conver_to_Hex()
        while self.resultado >0:
            #print("bit")
            valor = self.resultado%2
            self.lista.appendleft(valor)
            #print(self.convertido)
            self.resultado = self.resultado//2
            #print(resultado)
        for x in self.lista:
            self.convertido.append(x)
            #print(x)
        return self.convertido

'''inica = Conversorbit()
inica.resultado=50
inica.convertBit()'''



