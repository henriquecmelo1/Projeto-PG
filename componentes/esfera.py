import math
from .ponto import Ponto
from .material import Material
from .raio import Raio
from .vetor import Vetor

class Esfera:
    def __init__(self, centro: Ponto, raio_e, material: Material):
        self.centro = centro
        self.raio_e = raio_e
        self.material = material
        
    def hit(self, raio: Raio):
        oc = raio.origem - self.centro 

        # equacao segundo grau
        a = raio.direcao.dot(raio.direcao)
        b = 2.0 * oc.dot(raio.direcao)
        c = oc.dot(oc) - self.raio_e * self.raio_e
        discriminante = b*b - 4*a*c
        if discriminante >= 0:
            raiz = math.sqrt(discriminante)
            temp1 = (-b - raiz) / (2*a)
            temp2 = (-b + raiz) / (2*a)
            if temp1< 0 and temp2 < 0:
                return None
            if temp1 < 0:
                return temp2 #, ((raio.origem + temp2 * raio.direcao)-self.centro).unit_vector()
            if temp2 < 0:
                return temp1 #, ((raio.origem + temp1 * raio.direcao)-self.centro).unit_vector()
            if temp1 < temp2:
                return temp1 #, ((raio.origem + temp1 * raio.direcao)-self.centro).unit_vector()
            else:
                return temp2 #, ((raio.origem + temp2 * raio.direcao)-self.centro).unit_vector()
            

        return None
            
    
    def normal(self, ponto):
        return (ponto - self.centro) / self.raio_e