def encontrar_maximo(arreglo):
    if not arreglo:  # Si el arreglo está vacío, devuelve None
        return None
    maximo = arreglo[0]  # Supongamos que el primer elemento es el máximo inicialmente
    for num in arreglo:
        if num > maximo:
            maximo = num
    return maximo
resultado=encontrar_maximo([15, 15, 20])
print(resultado)