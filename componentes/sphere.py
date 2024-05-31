import math
from .hitable import Hitable
from .vec import Vec
import random

class Sphere(Hitable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, ray, t_min, t_max, rec): # Ray, float, float, HitRecord -> bool
        # calcula a interseção do raio com a esfera
        oc = ray.origin() - self.center # vetor do centro da esfera até a origem do raio

        # equação do segundo grau        
        a = ray.direction().dot(ray.direction()) 
        b = 2.0 * oc.dot(ray.direction()) 
        c = oc.dot(oc) - self.radius**2 
        discriminant = b**2 - 4*a*c 
        if discriminant > 0:
            root = math.sqrt(discriminant)
            temp = (-b - root) / (2*a)
            if t_min < temp < t_max: # se a raiz está no intervalo
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t) # ponto de interseção
                rec.normal = (rec.p - self.center) / self.radius
                rec.hit = True 
                return True 
            temp = (-b + root) / (2*a)
            if t_min < temp < t_max: # se a raiz está no intervalo
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t) # ponto de interseção
                rec.normal = (rec.p - self.center) / self.radius
                rec.hit = True
                return True
        return False
    
    def random_in_unit_sphere(): # None -> Vec
        # ponto aleatório na esfera unitária
        while True:
            e1 = 2*random.random() - 1
            e2 = 2*random.random() - 1
            e3 = 2*random.random() - 1

            p = Vec(e1, e2, e3)
            if p.dot(p) < 1:
                return p
