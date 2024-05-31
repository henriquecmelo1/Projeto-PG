class Ray:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def origin(self): # None -> Vec
        # Retorna a origem do raio
        return self.A

    def direction(self): # None -> Vec
        # Retorna a direção do raio
        return self.B

    def point_at_parameter(self, t): # float -> Vec
        # Retorna o ponto no raio a uma distância 't' da origem
        return self.A + t * self.B
