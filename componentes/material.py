from .cor import Cor

class Material:
    def __init__(self, cor: Cor, ambient, diffusion, specular, reflectity):
        self.cor = cor
        self.ambient = ambient
        self.diffusion = diffusion 
        self.specular = specular 
        self.reflectity = reflectity