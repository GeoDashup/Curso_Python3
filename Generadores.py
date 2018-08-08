def generaPares(Limite):

	num=1

	while num<Limite:

 		yield num*2

 		num=num+1


devuelvePares=generaPares(10)

print(next(devuelvePares))

print("Aqui podria ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))


#Generadores: Son estructuras que extraen valores de una función y se almacenan en objetos iterables(que se puede recorrer).
#Estos valores se almacenan de uno en uno.

#Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente.

#Esta caracterísitca es conocida como "supensión de estado"