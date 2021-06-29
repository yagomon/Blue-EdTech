# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

class Conta:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo

    def sacar(self, valor):
        self.saldo= self.saldo - valor
        print (f'Você sacou {valor} seu novo saldo é {self.saldo}') 

    def depositar(self, valor):
        self.saldo= self.saldo + valor
        print (f'Você depositou {valor} seu novo saldo é {self.saldo}') 

conta= Conta('Yago Monteiro', 4000)

print(conta.titular)
print()
print(conta.saldo)
print()
print(vars(conta))
print()

conta.sacar(1000)
print ()
conta.depositar(50)
print()
