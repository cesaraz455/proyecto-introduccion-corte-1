from models.automataCorreo import automataCorreo
from models.automataEntero import automataEntero
from models.automataId import automataId
from models.automataReales import automataReales

class automataController:

    def esEntero(self, valor):
        entero1 = automataEntero(valor)
        return entero1.Entero()

    def esCorreo(self, correo):
        correo1 = automataCorreo(correo)
        return correo1.Correo()

    def esReal(self, variable):
        real1 = automataReales(variable)
        return real1.Real()
    
    def esId(self, variable):
        id1 = automataId(variable)
        return id1.is_id()

    """def esIdentificador(self, identificador, cmpResult):
        indentificador1 = automataId()
        resultado = indentificador1.Id()"""