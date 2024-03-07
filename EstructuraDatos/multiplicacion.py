def multiplicacion_circular(matriz):
    multiplicacion = 1
    filas = len(matriz)
    columnas = len(matriz[0])


    for i in range(filas):
        for j in range(columnas):
            multiplicacion *= matriz[i][j]

    return multiplicacion



matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = multiplicacion_circular(matriz_ejemplo)
print("La multiplicación de los elementos de la matriz en forma circular es:", resultado)