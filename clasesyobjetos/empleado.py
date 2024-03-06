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

# Ejemplo de uso
empleado1 = Empleado("Juan", 30, "Masculino", 50000, "Desarrollador")
print("Nombre del empleado:", empleado1.obtener_nombre())
print("Edad del empleado:", empleado1.obtener_edad())
print("Género del empleado:", empleado1.obtener_genero())
print("Salario del empleado:", empleado1.obtener_salario())
print("Puesto de trabajo del empleado:", empleado1.obtener_puesto_de_trabajo())