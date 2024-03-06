class Empleado:
    empleados = []

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.empleados.append(self)

    @staticmethod
    def salario_promedio():
        if len(Empleado.empleados) == 0:
            return 0
        total_salario = sum(empleado.salario for empleado in Empleado.empleados)
        return total_salario / len(Empleado.empleados)


# Ejemplo de uso
empleado1 = Empleado("Juan", 3000)
empleado2 = Empleado("María", 4000)

print("Salario promedio de todos los empleados:", Empleado.salario_promedio())