from vocales import contar_vocales

while True:
    palabra = input('ingrese palabra o escribe "salir" para terminar : ')
    if palabra.lower() == 'salir': 
        break
    print(contar_vocales(palabra))
    