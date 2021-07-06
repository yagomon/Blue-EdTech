from random import choice
from time import sleep
from random import randint

class Personagem:
    def __init__(self):
        forca=10
        self.forca= forca

    def escolher_clima(self):
        self.tempo = ['Chuva','Sol']
        clima = choice(self.tempo)
        self.tempo = clima
       
class Heroi(Personagem):
    def __init__(self):
        super().__init__()
        self.vitalidade= 3

    def atacar(self,treino=0):
        self.força_adicional = treino

    def treinar(self):
        dic_treino = {5:'Seus exercícios matutinos foram muito bons e você ganhou +5 de força.',7:
        'Enquanto praticava seus exercícios choveu e você conseguiu ficar muito forte!\nSua força aumentou em +7 pontos.',3:'O de hoje ta pago! hahaha\nVocê ganhou + 3 de força.',2:'Houve um tempo de seca e suas raízes não tiveram de onde puxar nutrientes.\nVocê ganhou +2 de força', 4:'Você começou a treinar mais cedo e conseguiu dobrar seus exercicios!\nVocê ganha +4 de força.'}
        ganho_forca = choice(list(dic_treino.keys()))
        self.forca += ganho_forca
        print(dic_treino[ganho_forca]) 

class Vilao(Personagem):
    def __init__(self):
        super().__init__()
        forca= randint(1,5)



# Abretura do jogo
print('=-'*47)
print()

string = '███████╗██╗   ██╗██████╗ ███████╗██████╗    ''██████╗  █████╗ ████████╗ █████╗ ████████╗ █████╗ \n''██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    ''██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗\n''███████╗██║   ██║██████╔╝█████╗  ██████╔╝    ''██████╔╝███████║   ██║   ███████║   ██║   ███████║\n''╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    ''██╔══██╗██╔══██║   ██║   ██╔══██║   ██║   ██╔══██║\n''███████║╚██████╔╝██║     ███████╗██║  ██║    ''██████╔╝██║  ██║   ██║   ██║  ██║   ██║   ██║  ██║\n''╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    ''╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝'
for i in string: 
    sleep(0.001) 
    print(i, end='', flush=True)
print()
print()
print('=-'*47)

# Introdução ao jogo
string = "\nDona Blue comprou uma fazenda e começou a plantar alimentos orgânicos em sua horta.\nAlguns legumes e verduras não ficaram felizes com a suspensão dos agroTÓXICOS e começaram uma revolta!\n\nVocê é uma Super Batata orgânica e deve derrotar os vegetais dependentes químicos arruaceiros.\nMostre que é possível crescer forte e saudável sem depender de agroTÓXICOS.\n\nSó você pode derrotar os vilões e restaurar a ordem na Bluefarm!!!"
for i in string: 
    sleep(0.040) 
    print(i, end='', flush=True)
print()
print()

# Começo do jogo

batata= Heroi()
print(vars(batata))

print('Bom dia, Super Batata!\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm". O que deseja fazer?')
print('1- Treinar')
print('2- Derrotar alguns legumes arruaceiros')
escolha=input('')
while escolha not in ['1','2']:
     escolha = input('Entrada inválida!\n Digite 1 para treinar ou 2 para enfrentar algum vilão: ')

if escolha == 2:
    print('\nOs arruceiros estão plantados a mais tempo que você e se beneficiaram do uso de componentes tóxicos. Tem certeza que deseja ataca-los agora?')
    print('1- Sim. Eu sou uma Super Batata, irei ataca-los agora mesmo.')
    print('2-Não, acho melhor treinar um pouquinho antes.')
    confirma= input('')
    if confirma == 2:
        batata.treinar()
else:
    pass




# class Vilão(Personagem):
#     def __init__(self, força):
#         super().__init__(força)
#         self.viloes= ['cenoura','beterrava','alface','tomate','abobrinha','pepino','cebolinha','mandioca','rabanete','brocolis']

        
