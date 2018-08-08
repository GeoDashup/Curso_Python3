import sqlite3

miConexion=sqlite3.connect("GestiónProductos")

miCursor=miConexion.cursor()



miCursor.execute('''CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NOMBRE_ARTICULO VARCHAR (30),
	PRECIO INTEGER, 
	SECCIÓN VARCHAR(50))

''')


productos=[

	("Pelota", 20, "Juguetería"),
	("Pantalón", 15, "Confección"),
	("Destornillador", 25, "Ferretería"),
	("Jarrón", 45, "Cerámica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()