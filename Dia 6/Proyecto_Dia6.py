import os
from pathlib import Path
from os import system
import msvcrt

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
    if os.name == 'nt':  # Windows
        return system('cls')
    else:  # Linux, macOS
        return system('clear')



def mostrar_categorias(recetas):
    limpiar_consola()
    elementos = os.listdir(recetas)
    for id, categoria in enumerate(elementos):
        print(f'{id +1}. {categoria}')
    return (elementos)

def seleccionar_categoria(lista_categoria):
    sel_num_categoria = int(input('Seleccione el número de la categoría: '))
    categoria_seleccionada = lista_categoria[sel_num_categoria - 1]
    return categoria_seleccionada

def seleccionar_receta(lista_receta):
    sel_num_receta = int(input('Seleccione el número de la receta: '))
    receta = lista_receta[sel_num_receta - 1]
    return receta

def mostrar_recetas(categoria):
    link_txt = Path(categorias / categoria)
    archivos = os.listdir(link_txt)
    for id, archivo in enumerate(archivos):
        print(f'{id +1}. {archivo}')
    return archivos

def leer_eliminar_receta(opc):
    if opc == 1:
        print('receta dice...')
    else:
        print('receta eliminada')


def leer_crear_borrar(opc):
    lista_categoria= mostrar_categorias(categorias)
    categoria= seleccionar_categoria(lista_categoria)
    print(categoria)
    if opc == 1 or opc == 4:
        lista_receta= mostrar_recetas(categoria)
        receta = seleccionar_receta(lista_receta)
        print(receta)
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
    print('\nPresionar cualquier botón para continuar...')
    msvcrt.getch()
