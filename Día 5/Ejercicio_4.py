def contar_primos(num):
    lista = []
    repetidos = []
    for x in range(0, num):
        for y in range(2, x + 1):
            if x % y == 0:
                lista.append(x)

    for x in range(0, num):
        if lista.count(x) == 1:
            repetidos.append(x)
    cont = len(repetidos)
    return cont



print(contar_primos(3))
