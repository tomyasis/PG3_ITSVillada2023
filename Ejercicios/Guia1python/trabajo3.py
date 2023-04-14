anchura = int(input("Ingrese el ancho del rectángulo: "))
altura = int(input("Ingrese el alto del rectángulo: "))
caracter = input("Ingrese el caracter a utilizar en el dibujo: ")

for i in range(altura):
    for j in range(anchura):
        print(caracter, end="")
    print()