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

    def saludar(self):
        print(f"Hola, soy {self.nombre}. ¡Mucho gusto!")


class Empleado(Persona):
    def __init__(self, nombre, edad, genero, salario, puesto_de_trabajo):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.puesto_de_trabajo = puesto_de_trabajo

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, salario):
        self.salario = salario

    def obtener_puesto_de_trabajo(self):
        return self.puesto_de_trabajo

    def establecer_puesto_de_trabajo(self, puesto_de_trabajo):
        self.puesto_de_trabajo = puesto_de_trabajo

    def saludar(self):
        print(f"Hola, soy {self.nombre}, tu {self.puesto_de_trabajo}. ¡Mucho gusto!")


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

    def saludar(self):
        print(f"Hola, soy {self.nombre}, un estudiante de {self.grado} en {self.escuela}. ¡Mucho gusto!")

# Ejemplo de uso
persona1 = Persona("Carlos", 25, "Masculino")
empleado1 = Empleado("Laura", 35, "Femenino", 60000, "Gerente")
estudiante1 = Estudiante("Juan", 20, "Masculino", "Décimo grado", "Colegio ABC")

persona1.saludar()
empleado1.saludar()
estudiante1.saludar()