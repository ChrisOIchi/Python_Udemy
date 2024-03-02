mi_archivo= open('prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()