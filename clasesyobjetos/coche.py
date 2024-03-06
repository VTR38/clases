class Coche:
    def __init__(self):
        self.__velocidad = 0  # La velocidad se inicializa en 0

    def acelerar(self, cantidad):
        self.__velocidad += cantidad

    def frenar(self, cantidad):
        if self.__velocidad >= cantidad:
            self.__velocidad -= cantidad
        else:
            self.__velocidad = 0

    def obtener_velocidad(self):
        return self.__velocidad


# Ejemplo de uso
mi_coche = Coche()
mi_coche.acelerar(20)
print("Velocidad actual:", mi_coche.obtener_velocidad())  # Salida: Velocidad actual: 20
mi_coche.frenar(10)
print("Velocidad actual:", mi_coche.obtener_velocidad())