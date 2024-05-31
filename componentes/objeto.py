from abc import ABC, abstractmethod
from .material import Material
from .raio import Raio

class Objeto(ABC):
    def __init__(self, material: Material):
        self.material = material

    @abstractmethod
    def hit(self, raio: Raio):
        pass