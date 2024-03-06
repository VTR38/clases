def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    pivot = arreglo[len(arreglo)//2]
    menores = [x for x in arreglo if x < pivot]
    iguales = [x for x in arreglo if x == pivot]
    mayores = [x for x in arreglo if x > pivot]
    return quicksort(menores) + iguales + quicksort(mayores)

arreglo = [3, 6, 8, 10, 1, 2, 1]
arreglo_ordenado = quicksort(arreglo)
print(arreglo_ordenado)