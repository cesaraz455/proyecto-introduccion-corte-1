class AutomataEntero:
    def __init__(self, cadena):
        self.cadena = cadena
        self.estadoFinal = 2

    def Entero(self):
        self.estado = 1
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 1:
                if self.transicion == "+" or self.transicion == "-":
                    self.estado = 2
                elif str.isdigit(self.transicion):
                    self.estado = 2
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 2:
                if str.isdigit(self.transicion):
                    self.estado = 2
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser unicamente dígito"
            else:
                return False

        if self.estado == self.estadoFinal:
            return "Éxito: ¡El valor ingresado es un número entero!"
        else:
            return "Error: No hay valor ingresado en el campo de entero"

class AutomataReales:
    def __init__(self, cadena):
        self.cadena = cadena

    def Real(self):
        self.estado = 1
        for i in range(0, len(self.cadena)):
            self.transicion=self.cadena[i]
            if self.estado == 1:
                if self.transicion == "+" :
                    self.estado=2
                elif self.transicion == "-":
                    self.estado=3
                elif str.isdigit(self.transicion):
                    self.estado=4
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 2:
                if str.isdigit(self.transicion):
                        self.estado=4
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 3:
                if str.isdigit(self.transicion):
                        self.estado = 4
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 4:
                if self.transicion == ".":
                    self.estado = 5
                elif str.isdigit(self.transicion):
                    self.estado = 6
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 5:
                if str.isdigit(self.transicion):
                    self.estado = 6
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            elif self.estado == 6:
                if str.isdigit(self.transicion):
                    self.estado = 6
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
            else:
                return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
        if self.estado == 6:
            return "Éxito: El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"
        else:
            return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito o un + o -"

class AutomataCorreo:
    def __init__(self, texto):
        self.texto = texto

    def Correo(self):
        self.estado=1

        for i in range(0,len(self.texto)):

            self.transicion=self.texto[i]

        #print(self.estado,self.transicion)
            if self.estado == 1:
                if str.isalpha(self.transicion):
                    self.estado=2
                else:
                    return False
            elif self.estado == 2:
                if self.transicion == '@':
                    self.estado=3
                elif str.isalpha(self.transicion) or self.transicion =='_' or str.isdigit(self.transicion):
                    self.estado=2
                else:
                    return False
            elif self.estado == 3:
                if str.isalpha(self.transicion):
                    self.estado=4
                else:
                    return False
            elif self.estado == 4:
                if self.transicion == '.':
                    self.estado=5
                elif str.isalpha(self.transicion):
                    self.estado=4
                else:
                    return False
            elif self.estado == 5:
                if str.isalpha(self.transicion):
                    self.estado=6
                else:
                    return False
            elif self.estado == 6:
                if self.transicion == '.':
                    self.estado=7
                elif str.isalpha(self.transicion):
                    self.estado=6
                else:
                    return False
            elif self.estado == 7:
                if str.isalpha(self.transicion):
                    self.estado=8
                else:
                    return False
            elif self.estado == 8:
                if str.isalpha(self.transicion):
                    self.estado=8
                else:
                    return False
            else:
                return False
            #print(self.estado)
        if self.estado == 6 or self.estado == 8:
            #print("El correro: ",self.texto," es valido. \n")
            return True
        else:
            return False
