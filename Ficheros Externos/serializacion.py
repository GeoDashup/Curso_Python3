import pickle

lista_GOTY=["Hollow Knight", "Enter the Gungeon", "Ori and the Blind Forest", "Shovel Knight"]

fichero=open("lista_GOTY","wb")

pickle.dump(lista_GOTY, fichero)

fichero.close()

del (fichero)



#Serializacion: Consiste en guardar en un fichero externo una coleccion, un diccionario, un objeto.
#Con la particularidad es que la guardaremos en un fichero externo codigicado en código binario(succesión de bytes.