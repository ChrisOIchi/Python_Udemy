def suma(*args):
    total=0
    for num in args:
        total+=num
    return total

print(suma(5,6,4))