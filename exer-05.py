#Crie uma classe chamada 'Pessoa' com o atributo 'nome' e 'idade'. Implemente um método
#chamado 'falar' que imprime uma mensagem com nome da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def falar(self):
        print('Bom dia, eu me chamo {} e tenho {} naos de idade.'.format(self.nome, self.idade))

pessoa1 = Pessoa('Breno', 11)

pessoa1.falar()