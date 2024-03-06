class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia


class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # El coche tiene un motor

    def describir(self):
        return f"Coche: {self.marca} {self.modelo}, Motor: {self.motor.tipo}, Potencia: {self.motor.potencia}"


# Ejemplo de uso
motor_coche = Motor("Gasolina", "150CV")
coche = Coche("Toyota", "Corolla", motor_coche)

print(coche.describir())