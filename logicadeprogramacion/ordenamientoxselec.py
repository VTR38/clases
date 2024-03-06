def ordenamiento_por_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if arreglo[j] < arreglo[indice_minimo]:
                indice_minimo = j
        arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]
    return arreglo

arreglo = [3, 1, 4, 2, 5]
resultado = ordenamiento_por_seleccion(arreglo)
print(resultado)  # Output: [1, 2, 3, 4, 5]