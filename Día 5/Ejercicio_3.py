def doble_cero(*arg):
    if len(arg) <=1:
        return False

    for i, num in enumerate(arg):
        if i>0 and num ==0 and arg[i-1]==0:
            return True

    return False

print(doble_cero(1))  # Debe devolver False
print(doble_cero(0))  # Debe devolver False
print(doble_cero(0, 0))  # Debe devolver True
print(doble_cero(1, 2))  # Debe devolver False
print(doble_cero(0, 2, 0))  # Debe devolver False
print(doble_cero(1, 0, 0))  # Debe devolver True
print(doble_cero(0, 0, 0))  # Debe devolver True
print(doble_cero(0, 0, 1, 0))  # Debe devolver True
print(doble_cero(0, 1, 0, 1))  # Debe devolver False
print(doble_cero(0, 0, 0, 1, 0))  # Debe devolver True
