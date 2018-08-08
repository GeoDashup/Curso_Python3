print("Programa de becas Año 2017")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el nº de hermanos en el centro: "))
print(numero_hermanos)

salrio_familiar=int(input("Introduce salario anual bruto:"))
print(salrio_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salrio_familiar<=20000:

	print("Tienes derecho a beca")

else:

	print("No tienes derecho a beca")