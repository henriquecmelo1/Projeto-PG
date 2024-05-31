from .cor import Cor

class Resultado:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.pixels = [[Cor(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def set_pixel(self, i, j, cor: Cor):
        self.pixels[i][j] = cor

    def get_pixel(self, i, j):
        return self.pixels[i][j]
    
    
        