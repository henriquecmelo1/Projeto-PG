from .vetor import Vetor

class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vetor(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def sub_vetor(self, other):
        return Vetor(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Ponto):
            return False
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __str__(self):
        return f"{self.x} {self.y} {self.z}"
    
    def __repr__(self):
        return f"Ponto({self.x}, {self.y}, {self.z})"
    
    def __mul__(self, value):
        return Ponto(self.x * value, self.y * value, self.z * value)
    
    def __rmul__(self, value):
        return self.__mul__(value)
    
    
        