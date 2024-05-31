import math
from .ponto import Ponto
from .material import Material

class Esfera:
    def __init__(self, centro: Ponto, raio_e, material: Material):
        self.centro = centro
        self.raio_e = raio_e
        self.material = material
        
    def hit(self, raio):
        oc = raio.origem - self.centro

        # equacao segundo grau
        a = raio.direcao.dot(raio.direcao)
        b = 2.0 * oc.dot(raio.direcao)
        c = oc.dot(oc) - self.raio * self.raio
        discriminante = b*b - 4*a*c
        if discriminante > 0:
            raiz = math.sqrt(discriminante)
            temp = (-b - raiz) / (2*a)
            if temp > 0:
                return temp
            temp = (-b + raiz) / (2*a)
            if temp > 0:
                return temp
        return None
            
    
    def normal(self, ponto):
        return (ponto - self.centro) / self.raio