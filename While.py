#Como hacer que un bucle no sea infinito:

import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raíz cuadrada de un número negativo")

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break;

	numero=int(input("Introduce un número por favor: "))
	if numero<0:
		intentos+=1

if intentos<2:
	solution=math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solution))


