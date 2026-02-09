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
    
        
    def checkDni(self):
        self.setNumeroSano(self.__longitud() and self.__numero())
        return self.getNumeroSano()
    
    def __longitud(self):
        return len(self.dni) == 9 
    
    def __numero(self):
        return self.dni[:-1].isdigit()

    
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
        
    def getParteAlfabeticaDni(self):
        return self.dni[-1]

    def __setLetraSana(self, valor):
        self.letraSana = valor

    def __checkValida(self):
        return self.getParteAlfabeticaDni()