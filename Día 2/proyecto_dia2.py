nombre = input("¿Cual es su nombre?")
ventas=input("¿Cuánto vendió?")

comisiones=float(ventas)*0.13

print(f"Hola {nombre}, Usted vendió {ventas}, su comsisión es de {round(comisiones,2)}")