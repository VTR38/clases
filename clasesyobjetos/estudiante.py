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


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, grado, escuela):
        super().__init__(nombre, edad, genero)
        self.grado = grado
        self.escuela = escuela

    def obtener_grado(self):
        return self.grado

    def establecer_grado(self, grado):
        self.grado = grado

    def obtener_escuela(self):
        return self.escuela

    def establecer_escuela(self, escuela):
        self.escuela = escuela

# Ejemplo de uso
estudiante1 = Estudiante("María", 15, "Femenino", "Noveno grado", "Colegio XYZ")
print("Nombre del estudiante:", estudiante1.obtener_nombre())
print("Edad del estudiante:", estudiante1.obtener_edad())
print("Género del estudiante:", estudiante1.obtener_genero())
print("Grado del estudiante:", estudiante1.obtener_grado())
print("Escuela del estudiante:", estudiante1.obtener_escuela())