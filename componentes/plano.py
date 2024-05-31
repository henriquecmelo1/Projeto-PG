from .vetor import Vetor
from .ponto import Ponto
from .material import Material

class Plano:
    def __init__(self, ponto: Ponto, normal: Vetor, material: Material):
        self.ponto = ponto
        self.normal = normal.unit_vector()
        self.material = material

    def hit(self, raio):
        denominador = self.normal.dot(raio.direcao)
        if denominador != 0:
            temp = (self.ponto - raio.origem).dot(self.normal) / denominador
            if temp > 0:
                return temp
        return None

    def normal(self):
        return self.normal
    