def invertir_arreglo(arreglo):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio < fin:
        arreglo[inicio], arreglo[fin] = arreglo[fin], arreglo[inicio]

        inicio += 1
        fin -= 1


# Ejemplo de uso
arreglo = [1, 2, 3, 4, 5]
invertir_arreglo(arreglo)
print(arreglo)