def es_step(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        diferencia = abs(int(numero_str[i]) - int(numero_str[i+1]))
        if diferencia != 1:
            return False
    return True

num = input("ingrese un numero para calcular si es step o no: ")
print(es_step(num))