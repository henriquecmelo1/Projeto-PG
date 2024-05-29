from .ray import Ray

class Camera:
    def __init__(self, origin, lower_left_corner, horizontal, vertical):
        self.origin = origin
        self.lower_left_corner = lower_left_corner
        self.horizontal = horizontal
        self.vertical = vertical

    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)
