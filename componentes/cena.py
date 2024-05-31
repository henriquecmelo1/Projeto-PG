from .camera import Camera
from .cor import Cor
from .raio import Raio


class Cena:
    def __init__(self, camera: Camera, objetos):
        self.camera = camera
        self.objetos = []

    def ray_hit(self, raio: Raio):
        alvo = None
        dist_alvo = float('inf')

        for objeto in self.objetos:
            hit = objeto.hit(raio)
            if hit:
                if hit < dist_alvo:
                    alvo = objeto
                    dist_alvo = hit

        if alvo is not None:
            return alvo.material.cor
        else:
            return Cor(0, 0, 0)   

    def renderizar(self):
        camera = self.camera
        with open('output.ppm', 'w') as f:
            f.write(f"P3 {camera.width} {camera.height} 255\n")
            
            for i in range(camera.height):
                for j in range(camera.width):
                    raio = camera.get_ray(i, j)
                    cor = self.ray_hit(raio)
                    f.write(f'{cor.r()} {cor.g()} {cor.b()}\n')
            
        
    