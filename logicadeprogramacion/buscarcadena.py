def buscar_subcadena(cadena, subcadena):
    return cadena.find(subcadena)
cadena = "Hola Hola pacheco"
subcadena = "pacheco"
resultado = buscar_subcadena(cadena, subcadena)
print(resultado)