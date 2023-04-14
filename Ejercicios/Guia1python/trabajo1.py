def buscar_elemento(lista, elemento):
    """
    Busca el elemento en la lista y devuelve su índice si lo encuentra.
    Si el elemento no se encuentra en la lista, devuelve -1.
    """
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1
mi_lista = [8,12,9,45]
elemento_buscado = int(input("Ingresar un número: "))

indice = buscar_elemento(mi_lista, elemento_buscado)
if indice != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")