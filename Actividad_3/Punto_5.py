class Circulo:
    def _init_(self, centro, radio):
        self.radio = radio
        self.centro = centro

    def area(self):
        return f"el area del circulo es {pi * self.radio ** 2}"

    def perimetro(self):
        return f"el perimetro es {2 * pi * self.radio}"

    def pertenece_al_circulo(self, punto: Punto):
        # return punto.x <= self.radio and punto.y <= self.radio
        pass