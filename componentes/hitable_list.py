from .hitable import Hitable
from .hit_record import HitRecord

class HitableList(Hitable):
    def __init__(self, hitables):
        self.hitables = hitables

    def hit(self, ray, t_min, t_max, rec): # Ray, float, float, HitRecord -> bool
        # verifica se o raio atinge algum dos objetos
        hit_anything = False
        closest_so_far = t_max
        temp_rec = HitRecord()
        for hitable in self.hitables:
            if hitable.hit(ray, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
        return hit_anything
