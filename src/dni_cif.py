from src.tabla_asignacion import TablaAsignacion
class Dni:
    
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        self.tabla = TablaAsignacion


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

    def checkCIF(self):
        return self.checkDni() and self.checkLetra()

    def checkLongitud(self):
        return self.__longitud()
    
    def __longitud(self):
        return len(self.dni) == 9 and self.dni[:-1].isdigit() and self.dni[-1].isalpha()
    
    def checkCIF(self):
        return self.checkLongitud()
    
    
    def checkDni(self):
        self.setNumeroSano(self.__longitud())
        return self.getNumeroSano()
    
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
        
    # def getParteAlfabeticaDni(self):
    #    return self.dni[-1]