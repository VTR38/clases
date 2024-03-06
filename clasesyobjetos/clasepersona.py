class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero


persona1 = Persona("Juan", 30, "Masculino")
print("Nombre:", persona1.obtener_nombre())
print("Edad:", persona1.obtener_edad())
print("Género:", persona1.obtener_genero())


persona1.establecer_edad(35)
persona1.establecer_genero("Otro")

print("Edad modificada:", persona1.obtener_edad())
print("Género modificado:", persona1.obtener_genero())