class Hitable:
    def hit(self, ray, t_min, t_max, rec):
        raise NotImplementedError
