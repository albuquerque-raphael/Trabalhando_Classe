#Crie uma classe chamada 'retangulo', com atributo 'base' e 'altura, e implemente um método chamado 'calcular_area'
# que retorne a area do retângulo.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        area = self.base * self.altura
        return area

ret = Retangulo(6, 9)

print(ret.calcular_area())
        