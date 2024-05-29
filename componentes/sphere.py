import math
from .hitable import Hitable

class Sphere(Hitable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, ray, t_min, t_max, rec):
        oc = ray.origin() - self.center
        a = ray.direction().dot(ray.direction())
        b = 2.0 * oc.dot(ray.direction())
        c = oc.dot(oc) - self.radius**2
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root = math.sqrt(discriminant)
            temp = (-b - root) / (2*a)
            if t_min < temp < t_max:
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.hit = True
                return True
            temp = (-b + root) / (2*a)
            if t_min < temp < t_max:
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.hit = True
                return True
        return False