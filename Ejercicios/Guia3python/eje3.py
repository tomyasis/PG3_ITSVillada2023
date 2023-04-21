
while True:
    try:
        meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        num = int(input("Ingrese el numero de un mes -->  "))
        print(meses[num-1])
    except ValueError:
        print("Debe ingresar un numero entero")
    except IndexError:
        print("Ese numero no corresponde a uno relacionado a un mes")
    finally:
        cierre = input("Desea continuar (S/N) -->  ")
        if (cierre.lower()=="n"):
            break
