from tkinter import *
from tkinter import filedialog



root=Tk()


def abrirFichero():

	fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:", filetypes=(("Ficheros de Python", "*.py"),("Ficheros de texto", "*.txt"),("Todos los archivos", "*.*")))

	print(fichero)

Button(root, text="Abrir fichero", command=abrirFichero).pack()





root.mainloop()