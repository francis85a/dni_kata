class Dni:
    
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False


    def setDni (self, cadena):
        self.dni = cadena
    
    def getDni(self):
        return self.dni
    
    def setNumeroSano(self, valor):
        self.numeroSano = valor

    def getNumeroSano(self):
        return self.numeroSano
    
    def setLetraSana(self, valor):
        self.letraSana = valor

    def getLetraSana(self):
        return self.letraSana

    