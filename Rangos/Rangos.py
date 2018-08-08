valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):

	if email[i]=="@":

		valido=True


if valido:

	print("El email introducido \nes correcto")

else:

	print("El email introducido \nes incorrecto")

