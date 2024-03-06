class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Lista de empleados del departamento

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        for empleado in self.empleados:
            print(f"{empleado.nombre} - {empleado.cargo}")

# Ejemplo de uso
empleado1 = Empleado("Juan", "Programador")
empleado2 = Empleado("María", "Diseñador")

departamento = Departamento("Desarrollo")
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

print("Empleados del departamento de", departamento.nombre)
departamento.listar_empleados()