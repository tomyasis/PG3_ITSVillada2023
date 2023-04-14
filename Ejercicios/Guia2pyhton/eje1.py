class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("El nombre de usted es ", self.nombre)

Persona1 = Persona(input("Ingrese su nombre a continuacion: "))
Persona1.mostrar()