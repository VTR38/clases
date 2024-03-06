def buscar_elemento(arreglo, objetivo):
    return objetivo in arreglo

arreglo = [1, 2, 3, 4, 5]
objetivo = 3
resultado = buscar_elemento(arreglo, objetivo)
print(resultado)

objetivo = 4
resultado = buscar_elemento(arreglo, objetivo)
print(resultado)