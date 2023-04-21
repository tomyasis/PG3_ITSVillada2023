strings = ["¿Que tal?", "¿Como estas?", "¿bien?"]
num = 23
try:
    with open("guia3python/archivo.txt", "w") as f:
            for string in strings:
                f.write(string + "\n")
            f.write(num)
except TypeError:
    print("Error: No es posible escribir un entero en un archivo de texto.")