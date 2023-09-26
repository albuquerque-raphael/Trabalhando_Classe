#Crie uma classe chamada 'Conta Bancaria', que tenha o atributo 'saldo' e 'titular'. Implemente
#um método chamado 'depositar' e 'sacar' para manipular o saldo.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor 
        return self.saldo
    
conta1 = ContaBancaria(700, 'Luiz')

print(conta1.saldo, conta1.titular)

conta1.depositar(700)
print(conta1.saldo)

conta1.sacar(200)
print(conta1.saldo)