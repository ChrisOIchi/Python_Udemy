from pathlib import Path, PureWindowsPath

carpeta= Path('C:/Users/obedo/OneDrive/Documentos/Udemy Cursos/Python/Dia 6/pruebas.txt')
# if not carpeta.exists():
#     print('este archivo no existe')
# else:
#     print('existe')
# print(carpeta.suffix)

ruta_windows= PureWindowsPath(carpeta)
print(carpeta)
print(ruta_windows)