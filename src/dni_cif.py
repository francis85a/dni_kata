from src.tabla_asignacion import TablaAsignacion
class Dni:

    def __init__(self, dni=""):
        self.dni = dni
        self.numeroSano = False
        self.letraSana = False
        self.tabla = TablaAsignacion()


    def setDni (self, dni):
        self.dni = dni

    def getDni(self):
        return self.dni
    
    def setNumeroSano(self, valor):
        self.numeroSano = valor

    def getNumeroSano(self):
        return self.numeroSano
    
    def setLetraSana(self, letra):
        self.letraSana = letra

    def getLetraSana(self):
        return self.letraSana

    def checkCIF(self):
        return self.checkDni() and self.checkLetra()
    
        
    def checkDni(self):
        self.setNumeroSano(self.__longitud() and self.__checkNumero())
        return self.getNumeroSano()
    
    def __longitud(self):
        return len(self.dni) == 9 
    
    
    def checkLetra(self):
        if self.getNumeroSano():
            self.__setLetraSana(
                self.getParteAlfabeticaDni().isupper()
                and not self.getParteAlfabeticaDni().isdigit()
                and self.__checkValida()
            )
            return self.getLetraSana()
        else:
            
            return False

    def obtenerLetra(self):
        if self.getNumeroSano():
            return self.tabla.calcularLetra(self.getParteNumericaDni())
        else:
            return None

    def getParteAlfabeticaDni(self):
        return self.dni[-1]

    def __setLetraSana(self, valor):
        self.letraSana = valor

    def __checkValida(self):
        if self.getNumeroSano():
            return self.getParteAlfabeticaDni() == self.obtenerLetra()
    
    def __checkNumero(self):
        return self.dni[:-1].isdigit()
    
    def getParteNumericaDni(self):
        if self.getNumeroSano():
            return self.dni[:-1]
        else:
            return None
    