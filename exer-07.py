#Crie uma classe chamada 'Carro', com atributos: 'marca', 'modelo' e 'ano'. Implemente
#um método chamado 'detalhes', que retorne a uma string com as informações de carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def detalhes(self):
        print('Marca-> {}, Modelo-> {}, Ano-> {}'.format(self.marca, self.modelo, self.ano))
        
carro1 = Carro('Dodge', 'Dart', '2024')

carro1.detalhes()