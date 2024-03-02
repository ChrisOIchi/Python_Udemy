import os
from pathlib import Path
#
# ruta= os.chdir('C:\\Users\\obedo\\OneDrive\\Documentos\\Udemy Cursos\\Python\\Día 2')
#
# archivo=open('conversiones.py')
# print(archivo.read())
#
#ruta= os.makedirs('C:\\Users\\obedo\\OneDrive\\Documentos\\Udemy Cursos\\Python\\Día 2\\otra')
#
# ruta= 'C:\\Users\\obedo\\OneDrive\\Documentos\\Udemy Cursos\\Python\\Dia 6\\prueba.txt'
# #
# elemento= os.path.basename(ruta)
# print('el nombre del archivo'+ elemento)
#
# elemento= os.path.dirname(ruta)
# print('la ruta '+elemento)
#
# elemento= os.path.split(ruta)
# print(elemento)
#
# # eliminar carpetas
#
# os.rmdir('C:\\Users\\obedo\\OneDrive\\Documentos\\Udemy Cursos\\Python\\Día 2\\otra')

carpeta=Path("C:/Users/obedo/OneDrive/Documentos/Udemy Cursos/Python/Día 2")
archivo = carpeta / 'prueba1.txt'

mi_archivo=open(archivo)

print(mi_archivo.read())