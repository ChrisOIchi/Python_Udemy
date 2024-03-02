import os
from pathlib import Path
from os import system

base = Path.home()
categorias = Path(base / "Recetas")
opcion = 0
repetir = True


def desplegar_menu():
    print("""Bienvenido a su recetario
    1. Leer receta
    2. Crear receta
    3. Crear catagoria
    4. Borrar receta
    5. Borrar categoria
    6. Salir""")

    opcion = int(input('Selecciona una opción: '))
    limpiar_consola()
    return opcion


def limpiar_consola():
    return system('cls')


def mostrar_categorias(recetas):
    elementos=os.listdir(recetas)
    print(elementos)


def leer_eliminar_receta(opc):
    print('Seleccionar categoria')
    print('Seleccionar receta')
    if opc == 1:
        print('receta dice...')
    else:
        print('receta eliminada')


def leer_crear_borrar(opc):
    mostrar_categorias()
    if opc == 1 or opc == 4:
        print('leyendo o borrando receta')
        leer_eliminar_receta(opc)
    else:
        print('creando nueva receta')


while repetir:
    limpiar_consola()
    opcion = desplegar_menu()
    if opcion == 1 or opcion == 2 or opcion == 4:
        leer_crear_borrar(opcion)
    elif opcion == 3:
        print('Crear receta')
    elif opcion == 5:
        print('Borrar categoria')
    elif opcion == 6:
        print('Hasta pronto')
        repetir = False
    else:
        print('No es una opcion valida')
    input('\nPresionar cualquier botón para continuar...')
