
def contar_vocales (mi_string):
    vocales = ('a','á' , 'e', 'é' , 'i', 'í' , 'o', 'ó' , 'u', 'ú')
    resultado = {}
    mi_string_= mi_string.lower()
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado [letra] = 0
            resultado [letra] += 1 
    return resultado 




