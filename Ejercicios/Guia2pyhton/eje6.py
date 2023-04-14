class Familia:
    def __init__(self, nPad, nMad, nHijs):
        self.padre = nPad
        self.madre = nMad
        self.hijos = nHijs
    
    def __str__(self):
        return f"""
        Padre:{self.padre} 

        Madre: {self.madre}

        Hijos: {", ".join(self.hijos)}
        """

nomPadre = input("Ingresar el nombre del padre: ")
nomMadre = input("Ingresar el nombre de la madre: ")
hijos = []

while True:
    print("Ingrese - si usted no tiene mas hijos")
    a = input("Ingrese nombre de su hijo >>> ")
    if a != "-":
        hijos.append(a)
    else:
        break

familia = Familia(nomPadre, nomMadre, hijos)
print(familia)