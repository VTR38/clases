def eliminar_duplicados(arreglo):
    elementos_unicos = set()
    arreglo_sin_duplicados = []

    for num in arreglo:
        if num not in elementos_unicos:
            elementos_unicos.add(num)
            arreglo_sin_duplicados.append(num)

    return arreglo_sin_duplicados

arreglo = [1, 2, 3, 3, 4, 4, 5, 5, 5]
resultado = eliminar_duplicados(arreglo)
print(resultado)