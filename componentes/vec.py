import math

class Vec:
    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        self.e = [e0, e1, e2]
 
    def __getitem__(self, index):
        return self.e[index]
 
    def __setitem__(self, index, value):
        self.e[index] = value
 
    def x(self):
        return self.e[0]
 
    def y(self):
        return self.e[1]
 
    def z(self):
        return self.e[2]
 
    def r(self):
        return self.e[0]
 
    def g(self):
        return self.e[1]
 
    def b(self):
        return self.e[2]
 
    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"
 
    def __add__(self, other):
        return Vec(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])
 
    def __sub__(self, other):
        return Vec(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])
 
    def __mul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        else:  # multiplicação escalar
            return Vec(self.e[0] * other, self.e[1] * other, self.e[2] * other)
 
    # def __rmul__(self, other):
    #     return self.__mul__(other)
 
    def __truediv__(self, other): # divisão de um vetor por um escalar
        return Vec(self.e[0] / other, self.e[1] / other, self.e[2] / other)
 
    def dot(self, other): # produto escalar
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]
 
    def cross(self, other): # produto vetorial
        return Vec(self.e[1] * other.e[2] - self.e[2] * other.e[1],
                    self.e[2] * other.e[0] - self.e[0] * other.e[2],
                    self.e[0] * other.e[1] - self.e[1] * other.e[0])
 
    def length(self):
        return math.sqrt(self.dot(self))
 
    def unit_vector(self):
        return self / self.length()