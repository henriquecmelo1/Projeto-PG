class Hitable:
    def hit(self, ray, t_min, t_max, rec): # Ray, float, float, HitRecord -> bool
        # verifica se o raio atinge o objeto
        raise NotImplementedError
