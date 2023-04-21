while True:
    try:
        print("Se va a realizar la suma de dos numeros")
        num1 = float(input("Ingrese el primer numero -->  "))
        num2 = float(input("Ingrese el segundo numero -->  "))
        suma = num1+num2
        print(suma)
    except ValueError:
        print("Solo es valido ingresar numeros")
    finally:
        cierre = input("Desea continuar sumando(S/N) -->  ")
        if (cierre.lower()=="n"):
            break
