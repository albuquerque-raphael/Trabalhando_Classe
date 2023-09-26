#Crie uma classe chamada 'triangulo', com atributos 'lado1', 'lado2' e 'lado3', 
#implemente um método chamado 'calcular_perimetro', que retorne ao perímetro do triângulo

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return('O perímtro do triangulo é {}'.format(perimetro))
    
triangulo1 = Triangulo(7,6,5)

print(triangulo1.calcular_perimetro())