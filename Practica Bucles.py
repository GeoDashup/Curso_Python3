email=False
mi_email=input("Introduce tu dirección de email:")

for i in mi_email:

	if(i=="@"):

	    email=True


if email==True:
	print("El email es correcto")
else:
	print("El email no es correcto")
