def divide():

	try:

		op1=(float(input("Introdice el primer número: ")))

		op2=(float(input("Introdice el segundo número: ")))

		print("La división es: " + str(op1/op2))

	except ValueError:

		print("El valor introducido es ERRÓNEO")

	except ZeroDivisionError:

		print("No se puede dividir entre 0")

	finally:

		 print("Cálculo finalizado")

divide()

