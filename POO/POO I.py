#Programació orientada a objetos:

#¿En qué consite?:Trasladar la naturaleza de los objetos de la vida real al código de programción.

#¿Cuál es la naturaleza de un objeto de la vida real?: Los objetos tiene un estado, un comportamiento(¿Qué puede hacer?), y unas propiedades.



#Pongamos un ejemplo: El objeto coche.

#¿Cuál es el estado de un coche? Un coche puede estar parado. circulando, aparcado, etc.

#¿Qué propiedades tiene un coche? Un coche tiene color, un peso, un tamaño, etc.

#¿Qué comportamiento tiene un coche? Un coche puedde arancar, frenar, acelerar, girar, etc.



#Vocabulario de la POO:

#Clase: Modelo donde se redactan las características comunes de un grupo de objetos.

#Objeto: Es la materialización de la clase.

#Instancia de clase: Ejemplar perteneciente a una clase

#Modularización: 

#Encapsulamiento/encapsulación: Es encapsular una clase o propiedad.

     #self.__marca=marca

#Herencia: Es cuando una clase hereda las propiedades de otra clase.
class Vehiculos():
	
	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

class Furgoneta(Vehiculos):
	
		def carga(self, cargar):
			self.cargado=cargar


#Polimorfismo: Un objeto puede cambiar de forma dependiendo del contexto en el que se utilize. De la misma forma ese mismo objeto cambia de comportamientos.

class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")


class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")



def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)