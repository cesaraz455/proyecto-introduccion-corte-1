from models.automataModels import *

class automataController:

    def esEntero(self, valor):
        entero1 = AutomataEntero(valor)
        return entero1.Entero()

    def esReal(self, variable):
        real1 = AutomataReales(variable)
        return real1.Real()
    
    # def esCorreo(self, correo):
    #     correo1 = AutomataCorreo(correo)
    #     resultado = correo1.Correo()

    # def esIdentificador(self, identificador, cmpResult):
    #     indentificador1 = AutomataReales(variable)
    #     resultado = indentificador1.Real()