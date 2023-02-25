from tkinter import*
def pasardato():
    palabra.set(entrada.get())
ventana=Tk()
palabra=StringVar()
ventana.geometry("500x400")
ventana.title("colores")
lcolores=Label(ventana, text="Yeickon S", bg="black", fg="skyblue", font=('Algerian', 20)).pack()
ldata=Label(ventana,text="texto: ",textvariable=palabra).pack()
entrada=Entry(ventana)
entrada.pack()
boblack=Button(ventana, text="Negro",width=20,height=0,bg="gray", command=pasardato).pack()
bogray=Button(ventana, text="Gris",width=20,height=0,bg="gray").pack()

ventana.mainloop()