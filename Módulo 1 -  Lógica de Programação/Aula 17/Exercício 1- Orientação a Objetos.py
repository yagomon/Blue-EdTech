# Desafio 1- Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

from random import randint
from random import choice

class Lançador():
    def __init__(self,lados):
        self.lados= lados
        

    def lançar(self):
        if self.lados == 2:
            print(f'\nVocê tirou {choice["cara","coroa"]} na moeda.')
        elif self.lados == 6:
            print (f'\nVocê tirou o nº {randint(1,6)} no dado.')

jogo=input('Você desesaja lançar uma moeda ou um dado?\n 1- Dado\n 2- Moeda\n')
while jogo not in ['1', '2']:
    jogo=input('Você desesaja lançar uma moeda ou um dado?\n 1- Dado\n 2- Moeda\n')

if jogo == '1':
    lançarDado= Lançador(6)
    lançarDado.lançar()
elif jogo == "2":
    lançadorMoeda= Lançador(2)
    lançadorMoeda.lançar()   




