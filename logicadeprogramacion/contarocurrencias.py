def contar_ocurrencias(arreglo):
    contador = {}
    for elemento in arreglo:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

arreglo = [1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1]
resultado = contar_ocurrencias(arreglo)
print(resultado)