class CuentaBancaria:
    def __init__(self):
        self._saldo = 0  # Saldo protegido

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self._saldo}")


# Ejemplo de uso
cuenta = CuentaBancaria()
cuenta.depositar(1000)
cuenta.retirar(500)
cuenta.consultar_saldo()