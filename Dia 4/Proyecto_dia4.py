from random import randint

nombre= input("Cual es su nombre: ")
numero_aleatorio=randint(1,100)
turno = 8

print(f"""Bueno, {nombre}, he pensado en un número entre 1 y 100, y tienes solo 
        ocho intentos para adivinar cuál crees que es el número""")
# print(numero_aleatorio)

while turno >0:
    respuesta=input("Dime un número: ")
    turno-=1

    if int(respuesta) >100 or int(respuesta)<0:
        print("Escoge un número entre 1 y 100, el valor que ingresaste no es valido")
    elif int(respuesta) < numero_aleatorio:
        print("Intenta con un número mayor")
        print(f' Te quedan {turno} turnos')
    elif int(respuesta) > numero_aleatorio:
        print("Intenta con un número menor")
        print(f' Te quedan {turno} turnos')
    else:
        print("¡¡Correcto!!")
        print(f"Número de intentos: {8 - turno}")
        break

if turno==0:
    print(f"Se te acabaron los intentos, el numero era {numero_aleatorio}")
print('Game Over')