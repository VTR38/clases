from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

# Ejemplo de uso
rectangulo = Rectangulo(5, 3)
print("Área del rectángulo:", rectangulo.calcular_area())
print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())

circulo = Circulo(4)
print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())