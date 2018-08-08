print("Programa de evaluación de notas de alumnos")

nota_alumno=int(8)

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:                  
		valoracion="suspenso"   #Ámbito
	return valoracion           


print(evaluacion(nota_alumno))



def suma(num1, num2):
	
	resultado= num1 + num2

	return resultado
almacena_resultado=suma(5,8)

print(almacena_resultado)


#Operadores de comparación:

# < menor que
# > mayor que
# == igual que
# <= menor o igual que
# >= mayor o igual que
# != diferente que

