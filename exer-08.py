#Crie uma classe chamada 'Aluno' com atributos: 'nome' e 'notas'. Implemente um método
#chamado 'calcular_media' que retorne a média das notas dos anlunos.

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
aluno1 = Aluno('Rogério', 6.8, 8.1)

print(aluno1.calcular_media())