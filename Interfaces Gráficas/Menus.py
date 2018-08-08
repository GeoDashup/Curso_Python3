from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root=Tk()

def infoAdicional():

	messagebox.showinfo("Procesador de Ismael", "Procesador de textos v.2018")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	#valor=messagebox.askquestion("Salir", "Desea salir de la aplicación?")
	valor=messagebox.askokcancel("Salir", "Desea salir de la aplicación?")

	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento bloqueado")

	if valor==False:
		root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=600)

#-------------------------------------------------------------------------

archivoMenu=Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo documento                       Crtl+N")
archivoMenu.add_command(label="Abrir documento                       Crtl+O")
archivoMenu.add_command(label="Abrir carpeta")
archivoMenu.add_command(label="Guardar                                     Crtl+S")
archivoMenu.add_command(label="Guardar como...                       Crtl+Shift+S")
archivoMenu.add_separator()
archivoMenu.add_command(label="Nueva ventana")
archivoMenu.add_command(label="Cerrar ventana", command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicacion)

#-------------------------------------------------------------------------

archivoEdición=Menu(barraMenu, tearoff=0)

archivoEdición.add_command(label="Copiar                        Crtl+C")
archivoEdición.add_command(label="Cortar                        Crtl+X")
archivoEdición.add_command(label="Pegar                         Crtl+V")
archivoEdición.add_command(label="Undo                          Crtl+Z")
archivoEdición.add_command(label="Redo                          Crtl+Y")

#-------------------------------------------------------------------------

archivoHerramientas=Menu(barraMenu)

#-------------------------------------------------------------------------

archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

#-------------------------------------------------------------------------

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edición", menu=archivoEdición)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()