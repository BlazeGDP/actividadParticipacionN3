class CuentaBancaria:
    def _init_(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, nuevo_balance):
        self.balance += nuevo_balance

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto

    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02

    def mostrar_detalles(self):
        return f"El balance de la cuenta es de {self.balance}"