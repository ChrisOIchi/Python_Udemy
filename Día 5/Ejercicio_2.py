def clasificar_palabra(palabra):
    cadena = list(palabra.lower())
    quitar_repetidos = set(cadena)
    ordenado = list(quitar_repetidos)
    ordenado.sort()
    return ordenado


palabra = input("Ingresa palabra: ")

print(clasificar_palabra(palabra))
