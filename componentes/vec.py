import math



class Vec:
    def __init__(self, e0=0.0, e1=0.0, e2=0.0): # float, float, float -> None
        self.e = [e0, e1, e2]
 
    def __getitem__(self, index): # int -> float
        return self.e[index]
 
    def __setitem__(self, index, value): # int, float -> None
        self.e[index] = value

    #----------------- X Y Z -----------------
 
    def x(self): # None -> float
        return self.e[0]
 
    def y(self): # None -> float
        return self.e[1]
 
    def z(self): # None -> float
        return self.e[2]
    
    #----------------- R G B -----------------
 
    def r(self): # None -> float
        return self.e[0]
 
    def g(self): # None -> float
        return self.e[1]
 
    def b(self): # None -> float
        return self.e[2]
    
    #----------------- FUNCOES -----------------
 
    def __str__(self): # None -> str
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"
 
    def __add__(self, other): # Vec, Vec -> Vec
        return Vec(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])
 
    def __sub__(self, other): # Vec, Vec -> Vec
        return Vec(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])
 
    def __mul__(self, other): # Vec, Vec -> Vec // Vec, float -> Vec
        if isinstance(other, Vec):
            return Vec(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        else:  # multiplicação escalar
            return Vec(self.e[0] * other, self.e[1] * other, self.e[2] * other)
 
    def __rmul__(self, other): # float, Vec -> Vec
        return self.__mul__(other)
 
    def __truediv__(self, other): # Vec, float -> Vec
        # divisão de um vetor por um escalar
        return Vec(self.e[0] / other, self.e[1] / other, self.e[2] / other)
 
    def dot(self, other): # Vec, Vec -> float
        # produto escalar
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]
 
    def cross(self, other): # Vec, Vec -> Vec
        # produto vetorial
        return Vec(self.e[1] * other.e[2] - self.e[2] * other.e[1],
                    self.e[2] * other.e[0] - self.e[0] * other.e[2],
                    self.e[0] * other.e[1] - self.e[1] * other.e[0])
 
    def length(self): # Vec -> float
        # modulo do vetor
        return math.sqrt(self.dot(self))
 
    def unit_vector(self): # Vec -> Vec
        # vetor unitário
        return self / self.length()
    
    
            
    