from random import choice
from time import sleep
from random import randint


class Personagem:
    def __init__(self):
        forca=10   #força padrão de qualquer personagem
        self.forca= forca

    def escolher_clima(self):
        self.clima = ['chovendo','calor']  # clima que atua sobre qualquer personagem
        clima = choice(self.clima)
        self.clima = clima
        return self.clima
       
class Heroi(Personagem):
    def __init__(self):
        super().__init__()
        self.vitalidade= 3 # vida do Herói

    def atacar(self,treino=0):
        self.força_adicional = treino

    def treinar(self):
        dic_treino = {5:'Seus exercícios matutinos foram muito bons e você ganhou +5 de força.',7:
        'Enquanto praticava seus exercícios choveu e você conseguiu ficar muito forte!\nSua força aumentou em +7 pontos.',3:'O de hoje ta pago! hahaha\nVocê ganhou + 3 de força.',2:'Houve um tempo de seca e suas raízes não tiveram de onde puxar nutrientes.\nVocê ganhou +2 de força', 4:'Você começou a treinar mais cedo e conseguiu dobrar seus exercicios!\nVocê ganha +4 de força.'}
        ganho_forca = choice(list(dic_treino.keys()))
        
        if self.clima == 'chovendo':
            influencia_clima = 3
            self.forca += (ganho_forca + influencia_clima)
            print(dic_treino[ganho_forca])
            print('\n\nA chuva irrigou o solo da Bluefarm durante seus exercícios.\nVocê ganhou +3 de força.!')
            print(f'\nSua força total agora é: {self.forca}')
        else:
            print(dic_treino[ganho_forca]) 
            

class Vilao(Personagem):
    def __init__(self):
        super().__init__()
        ganho_forca= randint(1,5)
        self.forca += ganho_forca
         

    def escolher_vilão(self):
        lista_viloes= ['cenouras','beterrabas','alfaces','tomates','abobrinhas','pepinos','cebolinhas','mandiocas','rabanetes','brócolis']
        lista_jaForam = list()
        escolha_vilao = choice[lista_viloes] #Escolhe um vilão da lista_viloes

        while escolha_vilao in lista_jaForam:
            escolha_vilao = choice[lista_viloes] # Se o vilão escolhido já estiver na lista_jaForam escolhe novamente.

        lista_jaForam.append(escolha_vilao) # adiciona o vilão escolhido na lista dos vilões que já foram
        
        self.escolher_clima()
        if self.clima == 'calor': #influencia do clima na força do vilão escolhido
            self.força += 3
            print(f'\nHouve uma temporada de seca na horta dos arruaceiros, {escolha_vilao} desviaram a irrigação para eles e ganharam +3 de força.')     
        return escolha_vilao        
 
# Abertura do jogo


# Começo do jogo
batata= Heroi()
vilao= Vilao()

climaHeroi = batata.escolher_clima()

print()

if climaHeroi == 'chovendo': # Começo para dias de chuva
    sleep(1)
    print(f'Bom dia, Super Batata!')
    sleep(1.3)
    print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
    sleep(2.5)
    print('O que deseja fazer?')
    sleep(1.5)
    print('\n1- Treinar')
    sleep(1.3)
    print('2- Derrotar alguns vegetais arruaceiros')
    sleep(1.5)
    print('\nSituação do clima: chovendo')
    sleep(1)
    escolha=input('\nR:')
    while escolha not in ['1','2']:
        print('Entrada inválida!')
        sleep(1.2)
        print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
        sleep(2)
        print('Lembre-se, está chovendo!')
        sleep(1.8)
        escolha = input('R: ')
else: # Começo para dias de sol
    sleep(1)
    print(f'Bom dia, Super Batata!')
    sleep(1.3)
    print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
    sleep(2.5)
    print('O que deseja fazer?')
    sleep(1.5)
    print('\n1- Treinar')
    sleep(1.3)
    print('2- Derrotar alguns vegetais arruaceiros')
    sleep(1.5)
    print('\nSituação do clima: ensolarado')
    sleep(1)
    escolha=input('\nR:')
    while escolha not in ['1','2']:
        print('Entrada inválida!')
        sleep(1.2)
        print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
        sleep(2)
        print('Lembre-se, está ensolarado!')
        sleep(1.8)
        escolha = input('R: ')
        sleep(0.5)

# Testando as escolhas 
if escolha == '2':
    print('\nOs arruceiros estão plantados a mais tempo que você e se beneficiaram do uso de componentes tóxicos.\nTem certeza que deseja ataca-los?')
    sleep(5)
    print('\n1- Sim. Eu sou uma Super Batata, irei ataca-los agora mesmo!')
    sleep(1.5)
    print('2- Não, acho melhor treinar mais um pouquinho antes.')
    escolha= input('R: ')
    if escolha == '2':
        batata.treinar()
# Escolhendo inimigo aleatório
if escolha== '1':
    inimigos = vilao.escolher_vilão()
    print(f'Os arruaceiros da vez são {inimigos}.\nSó você, Super Batata, pode derrotar os inimigos e acabar com as raízes do mal! ')
    
    # Batalhando
    if batata.forca < vilao.forca:
        print(f'{inimigos:.2f}') 








        
