class Raio:
    def __init__(self, origem, direcao):
        self.origem = origem
        self.direcao = direcao.unit_vector()

    