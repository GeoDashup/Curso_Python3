import sqlite3

miConexion=sqlite3.connect("GestiónLibros")

miCursor=miConexion.cursor()


miCursor.execute('''CREATE TABLE LIBROS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NOMBRE_LIBRO VARCHAR(50), 
	AUTOR VARCHAR (50), 
	PRECIO INTEGER, 
	EDITORIAL VARCHAR (50))
''')

libros=[
	
	("M", "Lolita Bosch", 10, "Cruïlla"),
	("El Valle de los Lobos", "Laura Gallego", 15, "SM"),
	("El viaje de Doble-P", "Fernando Lalana", 8, "Bambú")


]


miCursor.executemany("INSERT INTO LIBROS VALUES (NULL,?,?,?,?)", libros)


miConexion.commit()

miConexion.close()