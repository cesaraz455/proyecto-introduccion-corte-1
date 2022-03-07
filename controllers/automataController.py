from models.automataCorreo import automataCorreo
from models.automataEntero import automataEntero
from models.automataReales import automataReales

class automataController:

    def esEntero(self, valor):
        entero1 = automataEntero(valor)
        return entero1.Entero()

    def esCorreo(self, correo):
        correo1 = automataCorreo(correo)
        return correo1.Correo()

    # def esReal(self, variable):
    #     real1 = AutomataReales(variable)
    #     return real1.Real()

    # def esIdentificador(self, identificador, cmpResult):
    #     indentificador1 = AutomataReales(variable)
    #     resultado = indentificador1.Real()