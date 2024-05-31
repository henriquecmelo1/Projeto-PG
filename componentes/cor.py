from .vetor import Vetor

class Cor(Vetor):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def r(self):
        return self.x
    def g(self):
        return self.y
    def b(self):
        return self.z
    