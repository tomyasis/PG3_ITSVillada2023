while True:
    try:
        print("Se va a realizar la division de dos numeros")
        num1 = float(input("Debe ingresar el primer numero -->  "))
        num2 = float(input("Debe ingresar el segundo numero -->  "))
        division = num1/num2
        print(division)
    except ValueError:
        print("Solo se pueden ingresar numeros")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        cierre = input("Desea continuar (S/N) -->  ")
        if (cierre.lower()=="n"):
            break
