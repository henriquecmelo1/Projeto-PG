from componentes import Camera, Cor, Esfera, Plano, Material, Ponto, Raio, Vetor, Cena
from PIL import Image
# from componentes.ponto import Ponto
# from componentes.vetor import Vetor
# from componentes.cor import Cor
# from componentes.material import Material
# from componentes.esfera import Esfera
# from componentes.plano import Plano
# from componentes.camera import Camera
# from componentes.cena import Cena
def view_ppm(file_path):
        img = Image.open(file_path)
        img.show()

def main():
    esfera1 = Esfera(Ponto(0, 0, 0), 1, Material(Cor(255, 0, 0), 0.5, 0.5, 0.5, 0.5))
    esfera2 = Esfera(Ponto(0, 1, 0), 1, Material(Cor(0, 255, 0), 0.5, 0.5, 0.5, 0.5))
    plano = Plano(Ponto(0, -1, 0), Vetor(0, 1, 0), Material(Cor(0, 0, 255), 0.5, 0.5, 0.5, 0.5))
    camera = Camera(Ponto(0, 0, -5), Ponto(0, 0, 0), Vetor(0, 1, 0), 1, 200, 200)


    cena = Cena(camera, [esfera1, esfera2, plano])
    cena.renderizar()
    view_ppm('output.ppm')
     
    




    

    









if __name__ == "__main__":
    main()