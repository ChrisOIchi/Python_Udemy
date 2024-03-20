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
    3. Crear categoria
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
        print(f'{id + 1}. {categoria}')
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
        print(f'{id + 1}. {archivo}')
    return archivos, link_txt


def leer_eliminar_receta(opc, receta, link_txt):
    archivo_texto = Path(link_txt, receta)
    if opc == 1:
        with open(archivo_texto, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    else:
        archivo_texto.unlink()
        print('La receta \'' + receta + '\' ha sido eliminada')


def leer_crear_borrar(opc):
    lista_categoria = mostrar_categorias(categorias)
    categoria = seleccionar_categoria(lista_categoria)
    print(categoria)
    if opc == 1 or opc == 4:
        lista_receta, link_txt = mostrar_recetas(categoria)
        receta = seleccionar_receta(lista_receta)
        leer_eliminar_receta(opc, receta, link_txt)
    else:
        nombre_receta = input("Nombre de la receta: ")
        texto = input("Ingrese la receta: ")
        link = Path(categorias, categoria, nombre_receta)

        with open(str(link) + ".txt", "w") as archivo:
            archivo.write(texto)

        print("Se ha guardado la receta de " + nombre_receta)


def crear_categoria():
    nueva_categoria = input('Escribe el nombre de la categoria nueva: ')
    link_categoria = Path(categorias, nueva_categoria)
    link_categoria.mkdir()
    print(nueva_categoria + " se ha creado")
    print(link_categoria)

def eliminar_categoria(categoria):
    link_categoria=Path(categorias,categoria)
    link_categoria.rmdir()
    print(categoria + ' ha sido eliminado')

while repetir:
    limpiar_consola()
    opcion = desplegar_menu()
    if opcion == 1 or opcion == 2 or opcion == 4:
        leer_crear_borrar(opcion)
    elif opcion == 3:
        crear_categoria()
    elif opcion == 5:
        lista_categorias= mostrar_categorias(categorias)
        categoria=seleccionar_categoria(lista_categorias)
        eliminar_categoria(categoria)
    elif opcion == 6:
        print('Hasta pronto')
        repetir = False
    else:
        print('No es una opcion valida')
    print('\nPresionar cualquier botón para continuar...')
    msvcrt.getch()
