class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        if self.nota >= 6:
            print (f"El alumno con el nombre {self.nombre} aprobo con una nota igual a", self.nota)
        else:
            print (f"El alumno con el nombre {self.nombre} desaprobo con una nota igual a", self.nota)

nombre1 = (input("Ingresar nombre del alumno: "))
nota1 = float(input("Ingresar la nota del alumno: "))

alumno1 = Alumno(nombre1, nota1)
alumno1.mostrar()