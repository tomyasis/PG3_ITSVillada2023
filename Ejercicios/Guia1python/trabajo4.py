def ordenar_lista(lista):
    return sorted(lista, reverse=True)
lista = [] 
while True:
    valor = input("Ingrese un valor para agregar a la lista o 'fin' para terminar: ")
    if valor == 'fin':
        break 
    lista.append(int(valor))  
print("La lista ingresada es:", lista)
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)