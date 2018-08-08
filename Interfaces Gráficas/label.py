from tkinter import *

root=Tk()

root.iconbitmap("Black Clover.ico")

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="Black Clover.png")

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()