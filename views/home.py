from controllers.automataController import automataController
from tkinter import *

class home:
    def __init__(self):
        self.automataController = automataController()
    
    def init(self):
        window = Tk()
        window.title("Validación de cadenas")
        window.geometry('650x300')
        lbl = Label(window, text="Numero Entero")
        lbl.grid(column=0, row=0)
        self.txt1 = Entry(window,width=10)
        self.txt1.grid(column=1, row=0)
        lbl2 = Label(window, text="Numero Real")
        lbl2.grid(column=0, row=1)
        self.txt2 = Entry(window,width=10)
        self.txt2.grid(column=1, row=1)
        lbl3 = Label(window, text="Numero notación científica")
        lbl3.grid(column=0, row=2)
        self.txt3 = Entry(window,width=10)
        self.txt3.grid(column=1, row=2)
        lbl4 = Label(window, text="Correo")
        lbl4.grid(column=0, row=3)
        self.txt4 = Entry(window,width=10)
        self.txt4.grid(column=1, row=3)
        self.cmpResult = Text(window,width=60,height=10)
        self.cmpResult.grid(row=5,column=0)
        btn = Button(window, text="Comprobar", command=self.clicked)
        btn.grid(column=2, row=0)
        window.mainloop()

    def clicked(self):
        self.cmpResult.delete('1.0', END)
        cadenaEntero = self.automataController.esEntero(self.txt1.get())
        cadenaReal = self.automataController.esReal(self.txt2.get())

        self.cmpResult.insert(INSERT, cadenaEntero + '\n' + cadenaReal)

        # self.automataController.esCorreo(self.txt3.get(), self.cmpResult)
        # self.automataController.esIdentificador(self.txt4.get(), self.cmpResult)