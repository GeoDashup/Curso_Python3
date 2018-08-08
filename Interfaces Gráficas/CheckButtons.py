from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():

	opcionesEscogida=""

	if(playa.get()==1):
		opcionesEscogida+= " Playa"

	if(montagna.get()==1):
		opcionesEscogida+=" Montaña"

	if(turismoRural.get()==1):
		opcionesEscogida+=" Turismo rural"

	textoFinal.config(text=opcionesEscogida)

foto=PhotoImage(file="images.png")
Label(root, image=foto).pack()

frame=Frame(root)

frame.pack()

Label(frame, text="Elige destino", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()