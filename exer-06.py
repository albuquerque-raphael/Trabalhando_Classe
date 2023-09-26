#Crie uma classe chamada 'Produto' com atributos 'nome', 'preco' e 'quantidade'. Implemente
#um método chamado 'calcular_total'que retorna o valor total do produto (preco * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def calcular_total(self):
        valor_total = self.preco * self.quantidade
        return valor_total
produto1 = Produto('Feijão', 10.90, 3)

print('Produto-> {}, Quantidade-> {}, Valor Total R$-> {:.3}'.format(produto1.nome, produto1.quantidade, produto1.calcular_total()))

        