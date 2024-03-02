from pathlib import Path

base=Path.home()
print(base)
guia=Path(base,'Barcelona', 'Sagrada_Familia.txt')
guia2=guia.with_name('La_Pedrera.txt')
print(guia.parent)
print(guia2)