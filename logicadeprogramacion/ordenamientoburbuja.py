def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

resultado = ordenamiento_burbuja([3, 2, 1, 5, 4])
print(resultado)