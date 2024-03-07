def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

entrada = input("Ingresa una lista de números separados por espacios: ")

numeros = [float(numero) for numero in entrada.split()]

suma_total = sumar_lista(numeros)

print("La suma de los números es:", suma_total)