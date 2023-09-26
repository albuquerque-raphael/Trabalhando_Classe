#Crie uma classe chamada 'Funcionário', com atributos: 'nome', 'salario', 'cargo'. Implemente
#um método chamado 'aumentar_salario' que receba um valor percentual de aumento e atualiza o 
#salário do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def aumentar_salario(self, percentual):
        self.salario = self.salario + (self.salario * (percentual/100))
        return self.salario
    
funcionario1 = Funcionario('Alfredo', 3000, 'Programador')
print(funcionario1.salario)

funcionario1.aumentar_salario(30)
print(funcionario1.salario)