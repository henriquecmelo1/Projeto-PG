from .ponto import Ponto
from .raio import Raio
from .vetor import Vetor

class Camera:
    def __init__(self, origin: Ponto, direction: Ponto, up: Vetor, distance, width, height):
        self.origin = origin #ponto
        self.direction = direction #ponto
        self.up = up #vetor
        self.distance = distance #float
        self.width = width #float
        self.height = height #float
        
    def vector_w(self):
        return (self.direction - self.origin).unit_vector()
    
    def vector_u(self):
        return self.up.cross(self.vector_w()).unit_vector()
    
    def vector_v(self):
        return self.vector_w().cross(self.vector_u())
    
    def move_to(self, point: Ponto):
        self.origin = point
        self.direction = point + self.vector_w() * self.distance
        self.up = self.vector_v()
        
    def move_direction(self, direction: Ponto):
        self.direction = self.origin + direction
        self.up = self.vector_v()

    def get_ray(self, x, y):
        center = self.origin + self.vector_w() * self.distance

        normalized_x = (x-self.width/2)/self.width
        normalized_y = (y-self.height/2)/self.height

        horizontal = self.vector_u() * normalized_x
        vertical = self.vector_v() * normalized_y

        return Raio(self.origin, center + horizontal + vertical - self.origin)






















# from .ray import Ray

# class Camera:
#     def __init__(self, origin, lower_left_corner, horizontal, vertical):
#         self.origin = origin
#         self.lower_left_corner = lower_left_corner
#         self.horizontal = horizontal
#         self.vertical = vertical

#     def get_ray(self, u, v): # float, float -> Ray
#         # Retorna um raio que passa pelo pixel na posição (u, v)
#         return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)
