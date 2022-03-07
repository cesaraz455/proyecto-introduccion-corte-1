class automataCorreo:
    def __init__(self, texto):
        self.texto = texto
        self.estadoFinal = "F"

    def isalpha(self, caracter):
        return (str.isalpha(caracter) or str.isdigit(caracter) or caracter == "-" or caracter == "_")

    def Correo(self):
        self.estado = "A"
        for i in range(0,len(self.texto)):
            self.transicion = self.texto[i]
            if self.estado == "A":
                if self.isalpha(self.transicion):
                    self.estado = "B"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un carácter alpha (numero, dígito, guión, guión bajo)"
            elif self.estado == "B":
                if self.isalpha(self.transicion):
                    self.estado = "B"
                elif self.transicion == "@":
                    self.estado = "C"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un arroba (@) o carácter alpha (numero, dígito, guión, guión bajo)"
            elif self.estado == "C":
                if self.isalpha(self.transicion):
                    self.estado = "D"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un carácter alpha (numero, dígito, guión, guión bajo)"
            elif self.estado == "D":
                if self.isalpha(self.transicion):
                    self.estado = "D"
                elif self.transicion == ".":
                    self.estado = "E"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un punto (.) o carácter alpha (numero, dígito, guión, guión bajo)" 
            elif self.estado == "E":
                if self.isalpha(self.transicion):
                    self.estado = "F"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un carácter alpha (numero, dígito, guión, guión bajo)"
            elif self.estado == "F":
                if self.isalpha(self.transicion):
                    self.estado = "F"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un carácter alpha (numero, dígito, guión, guión bajo)"

        if self.estado == self.estadoFinal:
            return "Éxito: ¡El valor ingresado es un número correo electrónico!"
        else:            
            return "Error: El valor ingresado no corresponde a un tipo correo electrónico, el automata no completo todos los estados"