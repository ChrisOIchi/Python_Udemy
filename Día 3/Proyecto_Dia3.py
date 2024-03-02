texto = input("Introduce un texto tan largo como quieras ")
letras = input("Agrega 3 letras que te gutaría contar en el texto, escribe las letras juntas ")

texto_minuscula = texto.lower()
letras = letras.lower()

a = letras[0]
b = letras[1]
c = letras[2]

# cuantas veces aparece
a_cont = texto_minuscula.count(a)
b_cont = texto_minuscula.count(b)
c_cont = texto_minuscula.count(c)

print(f"""La letra '{a}' aparece en el texto {a_cont} veces,
la letra '{b}' aparece {b_cont} veces y
la letra '{c}' aparece {c_cont} veces.""")

# contar la cantidad de palabras que tiene el texto

lista_texto= texto.split()
numero_palabras= len(lista_texto)

print(f"El texto cotiene {numero_palabras} palabra(s)")

# primera letra y última

primera_letra=texto[0]
ultima_letra=texto[-1]

print(f"La primera letra es '{primera_letra}' y la última letra es '{ultima_letra}'")

# Invertir el orden de las palabras
lista_texto.reverse()
texto_inv=' '.join(lista_texto)
print("Orden invertido de las palabras en el texto:")
print(texto_inv)

# Se encuentra la palabra 'Python'?
buscar_palabra=texto_minuscula.find("python")

respuesta={
    True: "La palabra Python si está en el texto",
    False:"La palabra Python no está en el texto"
}
x=buscar_palabra!=-1


print(respuesta[x])
