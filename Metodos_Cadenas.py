edad=input("Introduce la edad: ")


while(edad.isdigit()==False):

	print("Por favor, introduce un valor numérico")

	edad=input("Introduce la edad: ")

if(int(edad)<18):
	 print("No puede pasar")

else:

	print("Puedes pasar")


#upper(): Convierte en mayúsculas todas las letras de un String.

#lower(): Convierte en minúsculas todas las letras de un String.

#capitalize(): En un string hace que la primera letra sea mayúscula.

#count(): Cuenta cuantás veces se repite en una cadena de caracteres dentro de una frase.

#find(): Representar el índice en la cual aparece un caracter o un grupo de caracteres dentro de un texto.

#isdigit(): Devuelve un booleano(True, False). Nos dice si es valor introducido es un dígito o no.

#isalum(): Comprueba si es un alpha numérico.

#isalpha(): Comprueba si en un String solo hay letras(Los espacios tambien).

#split(): Separa por palabras utilizando espacios.

#strip(): Elimina los espacios sobrantes del principio y del final.

#replace(): Cambia una palabra o letra por otra dentro de un String.

#rfind(): Hace lo mismo que el find() pero empieza por detrás dentro del String.