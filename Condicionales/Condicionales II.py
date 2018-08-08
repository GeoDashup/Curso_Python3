salario_presidente=int(input("Introduce el salario presidente"))
print("Salarios presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario director"))
print("Salarios director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario presidente"))
print("Salarios Jefe Área: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario Administrativo"))
print("Salarios Administrativo: " + str(salario_administrativo))

if salario_presidente<salario_director<salario_administrativo<salario_jefe_area:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")