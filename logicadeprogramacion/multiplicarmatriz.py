def multiplicar_matrices(matriz1, matriz2):

    if len(matriz1[0]) != len(matriz2):
        return None

    resultado = [[0] * len(matriz2[0]) for _ in range(len(matriz1))]


    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]
resultado = multiplicar_matrices(matriz1, matriz2)
print(resultado)