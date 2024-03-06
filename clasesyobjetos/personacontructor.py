class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

# Ejemplo de uso
persona1 = Persona("Ana", 25, "femenino")
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Género:", persona1.genero)