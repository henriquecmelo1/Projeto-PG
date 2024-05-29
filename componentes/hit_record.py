from .vec import Vec

class HitRecord:
    def __init__(self):
        self.t = 0.0
        self.p = Vec()
        self.normal = Vec()
        self.hit = False
