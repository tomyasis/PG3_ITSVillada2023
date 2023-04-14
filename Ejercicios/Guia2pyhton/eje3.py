class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ladomayor(self):
        if self.lado1 != self.lado2:
            mayor = max(self.lado1, self.lado2, self.lado3)
            print(f"El lado mas grande es: {mayor} ")

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("El triangulo es equilatero, debido a que los tres lados son iguales")
        else:
            print("Este no es un triangulo equilatero")

lado1 = input("Ingrese el lado 1 >>> ")
lado2 = input("Ingrese el lado 2 >>> ")
lado3 = input("Ingrese el lado 3 >>> ")

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.ladomayor()
triangulo.equilatero()
