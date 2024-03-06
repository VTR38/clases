class Persona:
    contador = 0  # Variable de clase para realizar seguimiento del número total de personas creadas

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.contador += 1  # Incrementa el contador cada vez que se crea una nueva instancia de Persona

# Ejemplo de uso
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

print("Total de personas creadas:", Persona.contador)  # Imprime el número total de personas creadas