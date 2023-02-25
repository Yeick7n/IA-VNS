from tkinter import *
def sumar():
    num=int(Ent1.get())
    num2=int(Ent2.get())
    suma=num+num2
    variable.set(str(suma))

def restar():
    num=int(Ent1.get())
    num2=int(Ent2.get())
    resta=num-num2
    variable.set(+str(resta))

def multiplicar():
    num=int(Ent1.get())
    num2=int(Ent2.get())
    multiplica=num*num2
    variable.set(str(multiplica))

def dividir():
    num=int(Ent1.get())
    num2=int(Ent2.get())
    divide=num/num2
    variable.set(str(divide))

ventana = Tk()
variable=StringVar()
ventana.geometry("600x400")
ventana.title("CALCULADORA")
ventana.config(background="dimgray")

l1 = Label(ventana, text="Numero 1").grid(row=0, column=0)
l2 = Label(ventana, text="Numero 2").grid(row=1, column=0)
L3 = Label(ventana, text="Resultado: ").grid(row=2, column=0)

Ent1= Entry(ventana)
Ent1.grid(row=0, column=1)
Ent2 = Entry(ventana)
Ent2.grid(row=1, column=1)
Ent3 = Entry(ventana, textvariable= variable)
Ent3.grid(row=2, column=1)

Bsuma = Button(ventana, text="sumar", command=sumar).place(x=100, y=250)
Bresta = Button(ventana, text="restar", command=restar).place(x=150, y=250)
Bmultipli = Button(ventana, text="multiplicar", command=multiplicar).place(x=200, y=250)
Bdivision = Button(ventana, text="dividir", command=dividir).place(x=275, y=250)
Bsalir = Button(ventana, text="salir").place(x=50, y=250)

ventana.mainloop()
