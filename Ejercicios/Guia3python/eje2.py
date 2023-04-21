while True:
    try:
        print("Se va a realizar la suma de dos numeros")
        num1 = float(input("Ingrese el primer numero -->  "))
        num2 = float(input("Ingrese el segundo numero -->  "))
        division = num1/num2
        print(division)
    except ZeroDivisionError:
        print("No es valido dividir por cero")
    finally:
        cierre = input("Desea continuar (S/N) -->  ")
        if (cierre.lower()=="n"):
            break
