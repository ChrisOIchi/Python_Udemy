from random import choice

palabras = [
    "manzana", "pera", "banana", "uva", "sandia", "melon", "pina", "mango", "papaya", "naranja",
    "perro", "gato", "pez", "pajaro", "elefante", "jirafa", "leon", "tigre", "oso", "serpiente",
    "coche", "ordenador", "telefono", "mesa", "silla", "libro", "reloj", "casa", "ventana", "puerta",
    "sol", "luna", "estrella", "nube", "arcoiris", "montana", "rio", "mar", "oceano", "bosque",
    "amor", "felicidad", "paz", "sueno", "aventura", "misterio", "magia", "energia", "creatividad", "amistad",
    "alegria", "dolor", "cambio", "tiempo", "historia", "vida", "muerte", "futuro", "pasado", "presente"
]


def ocultar_palabra(palabra):
    cont = len(palabra)
    guion = "_" * cont
    return guion


def sustituir_letra(palabra, caracter, palabra_censurada):
    lista_palabra = list(palabra_censurada)
    for i, letra in enumerate(palabra):
        if caracter == letra and i < len(lista_palabra):
            lista_palabra[i] = caracter
    nueva_palabra_censurada = ''.join(lista_palabra)
    return nueva_palabra_censurada


def verificar_letra(palabra, letra, palabra_oculta):
    global cont
    if letra in palabra:
        print("si está")
        palabra_oculta = sustituir_letra(palabra, letra, palabra_oculta)
        return palabra_oculta
    else:
        print("no está")
        cont += 1
        print(f"Error {cont}")
    return palabra_oculta


def contar_menciones(letra):
    apariciones = palabra.count(letra)
    return apariciones


def elegir_letra():
    caracter = ""
    while len(caracter) !=1 or not caracter.isalpha():
        caracter = input("Ingresa una letra: ")
    return caracter


# elegir palabra aleatoria
palabra = choice(palabras)
# print(palabra)
# ocultar palabra
palabra_oculta = ocultar_palabra(palabra)
print(palabra_oculta)
cont = 0

# Iniciar intentos
while cont < 6:
    caracter = elegir_letra()
    palabra_oculta = verificar_letra(palabra, caracter, palabra_oculta)
    print(palabra_oculta)
    if "_" not in palabra_oculta:
        print("Ganaste")
        break
else:
    print("¡Perdiste! La palabra era: ", palabra)
