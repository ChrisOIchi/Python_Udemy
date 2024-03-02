def devolver_distintos(lista):
    suma = sum(lista)
    minimo=min(lista)
    maximo=max(lista)
    intermedio=0
    if suma>15:
        print(f"El numero mayor es: {maximo}")
    elif suma<10:
        print(f"El numero menor es: {minimo}")
    else:
        for num in lista:
            if num!=maximo and num!=minimo:
                intermedio=num
        print(f"El valor intermedio es: {intermedio}")

cont=0
lista = []
while cont<3:
    lista.append(int(input("Ingresa un numero: ")))
    cont +=1

devolver_distintos(lista)