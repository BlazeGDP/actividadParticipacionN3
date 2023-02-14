class Punto:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        return f"({self.x} , {self.y})"

    def mover(self, nuevoX, nuevoY):
        self.x = nuevoX
        self.y = nuevoY

    def calcular_distancia(self, x, y):
        return f"la distancia es  entre los puntos es de {((x - self.x) * 2 + (y - self.y) * 2) * (1 / 2)}"