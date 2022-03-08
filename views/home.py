from controllers.automataController import automataController
from tkinter import *

class home:
    def __init__(self):
        self.automataController = automataController()
    
    def init(self):
        window = Tk()
        window.title("Validación de cadenas mediante Automatas")
        window.geometry('700x250')

        # Primera fila
        lblEntero = Label(window, text="Numero Entero")
        lblEntero.grid(column=0, row=0)
        self.txtEntero = Entry(window, width=10)
        self.txtEntero.grid(column=1, row=0)
        btnEntero = Button(window, text="Comprobar", command=self.clickedEntero)
        btnEntero.grid(column=2, row=0)

        # Segunda fila
        lblCorreo = Label(window, text="Correo electrónico")
        lblCorreo.grid(column=0, row=1)
        self.txtCorreo = Entry(window, width=10)
        self.txtCorreo.grid(column=1, row=1)
        btnCorreo = Button(window, text="Comprobar", command=self.clickedCorreo)
        btnCorreo.grid(column=2, row=1)

        # Tercera fila
        lblReal = Label(window, text="Numero Real")
        lblReal.grid(column=0, row=2)
        self.txtReal = Entry(window, width=10)
        self.txtReal.grid(column=1, row=2)
        btnReal = Button(window, text="Comprobar", command=self.clickedReal)
        btnReal.grid(column=2, row=2)

        # Cuarta fila
        lblIdentificador = Label(window, text="Identificador")
        lblIdentificador.grid(column=0, row=3)
        self.txtIdentificador = Entry(window, width=10)
        self.txtIdentificador.grid(column=1, row=3)
        btnIdentificador = Button(window, text="Comprobar", command=self.clickedIdentificador)
        btnIdentificador.grid(column=2, row=3)

        self.cmpResult = Text(window,width=60,height=10)
        self.cmpResult.grid(row=4,column=0)

        window.mainloop()

    def clickedEntero(self):
        self.cmpResult.delete('1.0', END)
        cadenaEntero = self.automataController.esEntero(self.txtEntero.get())
        self.cmpResult.insert(INSERT, "Validación de entero:\n" + cadenaEntero)

    def clickedCorreo(self):
        self.cmpResult.delete('1.0', END)
        cadenaCorreo = self.automataController.esCorreo(self.txtCorreo.get())
        self.cmpResult.insert(INSERT, "Validación de correo electrónico:\n" + cadenaCorreo)

    def clickedReal(self):
        self.cmpResult.delete('1.0', END)
        cadenaReal = self.automataController.esReal(self.txtReal.get())
        self.cmpResult.insert(INSERT, "Validación de real\n" + cadenaReal)

    def clickedIdentificador(self):
        self.cmpResult.delete('1.0', END)
        cadenaIdentificador = self.automataController.esId(self.txtIdentificador.get())
        self.cmpResult.insert(INSERT, "Validación de identificador\n" + cadenaIdentificador)