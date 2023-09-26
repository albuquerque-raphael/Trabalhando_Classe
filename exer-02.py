#Crie uma classe chamada 'Livro' que tenha o atributo 'titulo' e 'autor', implemente um método
#chamado detalhes que retorne uma string com as informações do livro

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def detalhes(self):
        print('Título -> {} / Autor -> {}'.format(self.titulo, self.autor))
        
livro = Livro('A Biblia no meu dia a dia', 'Pe Jonas Abib')

livro.detalhes()