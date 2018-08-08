from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(1,0)

raiz.iconbitmap("Black Clover.ico")

#raiz.geometry("650x350")

raiz.config(bg="black")

raiz.config(bd=14)

raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=14)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

raiz.mainloop()

