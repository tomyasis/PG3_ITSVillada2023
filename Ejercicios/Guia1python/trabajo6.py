def contar_vocales(frase):
    frase = frase.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

a = input("Ingrese una frase: ")
print(contar_vocales(a))