
class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Vetor):
            return False
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __add__(self, v):
        return Vetor(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __sub__(self, v):
        return Vetor(self.x - v.x, self.y - v.y, self.z - v.z)
    
    def __mul__(self, v):
        if isinstance(v, Vetor):
            return Vetor(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return Vetor(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __truediv__(self, v):
        return Vetor(self.x / v, self.y / v, self.z / v)

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v):
        return Vetor(self.y * v.z - self.z * v.y, 
                     self.z * v.x - self.x * v.z, 
                     self.x * v.y - self.y * v.x)  

    def length(self):
        return (self.dot(self)) ** 0.5
    
    def unit_vector(self):
        return self / self.length()
   