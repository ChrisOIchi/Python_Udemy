lista= ['hola ', 'mundo ', 'aqui', 'estoy']
archivo=open('prueba.txt', 'a')
for p in lista:
    archivo.writelines(p + "\n")

archivo.close()