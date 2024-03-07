def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados


mi_lista = [1, 2, 3, 4, 2, 3, 5, 5, 5, 5, 1, 2, 3, 4, 5, 20]
resultado = eliminar_duplicados(mi_lista)
print("Lista original:", mi_lista)
print("Lista sin duplicados:", resultado)