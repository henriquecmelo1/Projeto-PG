from PIL import Image
import random
from componentes import Vec, Ray, HitRecord, HitableList, Sphere, Camera

def view_ppm(file_path):
    img = Image.open(file_path)
    img.show()

# def hit_sphere(center, radius, r):
#     oc = r.origin() - center
#     a = r.direction().dot(r.direction())
#     b = 2.0 * oc.dot(r.direction())
#     c = oc.dot(oc) - radius * radius
#     discriminant = b*b - 4*a*c

#     return discriminant > 0

# def color(r):
#     if hit_sphere(Vec(0, 0, -1), 0.5, r):
#         return Vec(1, 0, 0) # retorna a cor vermelha
#     unit_direction = Vec.unit_vector(r.direction())
#     t = 0.5 * (unit_direction.y() + 1.0)
#     temp1 = Vec.__mul__(Vec(1.0, 1.0, 1.0), (1.0-t))
#     temp2 = Vec.__mul__(Vec(0.5, 0.7, 1.0), t)
#     return Vec.__add__(temp1, temp2)

def color(ray, world):
    rec = HitRecord()
    if world.hit(ray, 0.1, float('inf'), rec):
        return 0.5 * (rec.normal + Vec(1, 1, 1))  # Visualização das normais como cores
    else:
        unit_direction = ray.direction().unit_vector()
        t = 0.5 * (unit_direction.y() + 1.0)
        return Vec(1.0, 1.0, 1.0) * (1.0 - t) + Vec(0.5, 0.7, 1.0) * t


def main():
    nx, ny = 200, 100
    ns = 100  # números de amostras para antialiasing

    lower_left_corner = Vec(-2.0, -1.0, -1.0)
    horizontal = Vec(4.0, 0.0, 0.0)
    vertical = Vec(0.0, 2.0, 0.0)
    origin = Vec(0.0, 0.0, 0.0)

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
                    col += color(ray, world)
                
                col /= ns
                ir, ig, ib = int(255.99 * col.r()), int(255.99 * col.g()), int(255.99 * col.b())
                out.write(f"{ir} {ig} {ib}\n")
 
if __name__ == "__main__":
    main()
 