#Crie uma área chamada 'Circulo' que tenha atributo 'raio', implemente um método chamado calcular_area
# que retorne a área do circulo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        area = 2.60 * (self.raio ** 2)
        return area
    
c1 = Circulo(4)

print(c1.calcular_area())