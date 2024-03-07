def tienen_elemento_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

# Ejemplo de uso de la función
lista_a = [1, 2, 3, 4, 5]
lista_b = [7, 6, 7, 8, 9]
print(tienen_elemento_comun(lista_a, lista_b))  # Salida esperada: True