def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valore es {num1}')
    print(f'El segundo valore es {num2}')
    for arg in args:
        print(f'arg= {arg}')

    for clave, valor in kwargs.items():
        print(clave, valor)


prueba(15, 50, 50, 40, 30, 200, x=3, y=5, z=2)