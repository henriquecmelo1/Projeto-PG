import math
from PIL import Image
import sys
from componentes import Vec, Ray

def view_ppm(file_path):
    img = Image.open(file_path)
    img.show()

def hit_sphere(center, radius, r):
    oc = r.origin() - center
    a = r.direction().dot(r.direction())
    b = 2.0 * oc.dot(r.direction())
    c = oc.dot(oc) - radius * radius
    discriminant = b*b - 4*a*c

    return discriminant > 0

def color(r):
    if hit_sphere(Vec(0, 0, -1), 0.5, r):
        return Vec(1, 0, 0) # retorna a cor vermelha
    unit_direction = Vec.unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1.0)
    temp1 = Vec.__mul__(Vec(1.0, 1.0, 1.0), (1.0-t))
    temp2 = Vec.__mul__(Vec(0.5, 0.7, 1.0), t)
    return Vec.__add__(temp1, temp2)

def main():
    nx = 200
    ny = 100
    lower_left_corner = Vec(-2.0, -1.0, -1.0)
    horizontal = Vec(4.0, 0.0, 0.0)
    vertical = Vec(0.0, 2.0, 0.0)
    origin = Vec(0.0, 0.0, 0.0)

    with open("output.ppm", "w") as out:
        out.write("P3\n{} {}\n255\n".format(nx, ny)) # Cabeçalho do arquivo PPM
        for j in range(ny-1, -1, -1):
            for i in range(nx):
                u = float(i) / float(nx)
                v = float(j) / float(ny)
                r = Ray(origin, lower_left_corner + Vec.__mul__(horizontal, u)+ Vec.__mul__(vertical, v))
                col = color(r)
                ir = int(255.99 * col.x())
                ig = int(255.99 * col.y())
                ib = int(255.99 * col.z())
                # print(f"{ir} {ig} {ib}")
                out.write(f"{ir} {ig} {ib}\n")
    # view_ppm('output.ppm')
    
 
if __name__ == "__main__":
    main()
 