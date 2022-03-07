class automataReales:
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