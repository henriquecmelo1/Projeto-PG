import math
from PIL import Image
import sys
from componentes import Vec, Ray

def view_ppm(file_path):
    img = Image.open(file_path)
    img.show()

def color(r):
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
    for j in range(ny-1, -1, -1):
        for i in range(nx):
            u = float(i) / float(nx)
            v = float(j) / float(ny)
            r = Ray(origin, lower_left_corner + Vec.__mul__(horizontal, u)+ Vec.__mul__(vertical, v))
            col = color(r)
            ir = int(255.99 * col.x())
            ig = int(255.99 * col.y())
            ib = int(255.99 * col.z())
            print(f"{ir} {ig} {ib}")
    view_ppm('output.ppm')
    
 
if __name__ == "__main__":
    main()
 