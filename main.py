from PIL import Image
import random
import numpy as np
from componentes import Vec, Ray, HitRecord, HitableList, Sphere, Camera

def view_ppm(file_path):
    img = Image.open(file_path)
    img.show()


def color(r, world):
    rec = HitRecord()
    if world.hit(r, 0.0, float('inf'), rec): # se o raio atinge um objeto
        target = rec.p + rec.normal + Vec.random_in_unit_sphere() # ponto aleatório na esfera unitária
        return 0.5 * color(Ray(rec.p, target - rec.p), world) # recursão
    else:
        unit_direction = Vec.unit_vector(r.direction()) # vetor unitário
        t = 0.5 * (unit_direction[1] + 1.0) # interpolação linear
        return (1.0 - t) * Vec(1.0, 1.0, 1.0) + t * Vec(0.5, 0.7, 1.0) # cor do céu
    



def main():
    nx, ny = 200, 100
    ns = 100  # números de amostras para antialiasing

    # Camera
    lower_left_corner = Vec(-2.0, -1.0, -1.0)
    horizontal = Vec(4.0, 0.0, 0.0)
    vertical = Vec(0.0, 2.0, 0.0)
    origin = Vec(0.0, 0.0, 0.0)

    # World
    camera = Camera(origin, lower_left_corner, horizontal, vertical)
    world = HitableList([Sphere(Vec(0, 0, -1), 0.5), Sphere(Vec(0, -100.5, -1), 100)])

    with open("output.ppm", "w") as out:
        out.write(f"P3\n{nx} {ny}\n255\n")
        for j in range(ny-1, -1, -1):
            for i in range(nx):
                col = Vec(0, 0, 0)

                for s in range(ns):
                    u = (i + random.random()) / nx
                    v = (j + random.random()) / ny
                    ray = camera.get_ray(u, v)
                    col = col + color(ray, world)
                
                col /= ns # média das amostras
                col = Vec(np.sqrt(col[0]), np.sqrt(col[1]), np.sqrt(col[2])) # gamma correction
                ir = int(255.99 * col[0])
                ig = int(255.99 * col[1])
                ib = int(255.99 * col[2])
                out.write(f"{ir} {ig} {ib}\n")

    view_ppm('output.ppm')

    
 
if __name__ == "__main__":
    main()
 