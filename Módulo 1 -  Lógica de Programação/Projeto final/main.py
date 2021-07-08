from random import choice
from time import sleep
from random import randint
# from abertura import abertura
from gameover import gameover

class Personagem:
    def __init__(self,clima):
        forca=10   #força padrão de qualquer personagem
        self.forca= forca
        self.clima= clima
        self.nome= ''
       
class Heroi(Personagem):
    def __init__(self,clima):
        super().__init__(clima)
        self.vitalidade= 3 # vida do Herói
        self.clima= clima

    def treinar(self):
        dic_treino = {5:'Seus exercícios matutinos foram muito bons e você ganhou +5 de força.',7:
        'Enquanto praticava seus exercícios a terra foi adubada e você ficou muito forte!\nSua força aumentou em +7 pontos.',3:'O de hoje ta pago...hahahahaha!\nVocê ganhou + 3 de força.',2:'Uma nuvem de gafanhotos passou pela orta e seus treinos não renderam.\nVocê ganhou +2 de força', 4:'Você começou a treinar mais cedo e conseguiu dobrar seus exercicios!\nVocê ganha +4 de força.'}
        ganho_forca = choice(list(dic_treino.keys()))
        self.forca += ganho_forca

        if self.clima == 'chovendo':
            influencia_clima = 3
            self.forca += influencia_clima

            print()
            sleep(0.5)
            print('🌨 '*45)
            sleep(1)
            print(dic_treino[ganho_forca])
            sleep(4)
            print('\nA chuva irrigou o solo da Bluefarm.\nVocê ganhou +3 de bônus!')
            sleep(1.5)
            print(f'\nSua força total agora é: {self.forca} pts')
            sleep(1)
            print('🌨 '*45)
            sleep(2)
            print('\nVá para casa descansar, pois amanhã será um longo dia...........')
            for i in range(60):
                print('.',end='', flush=True )
                sleep(0.05)
            print('.'*60)
        else:
            print()
            sleep(0.5)
            print('-='*60)
            sleep(1)
            print(dic_treino[ganho_forca])
            sleep(1.5) 
            print(f'\nSua força total agora é: {self.forca} pts')
            sleep(1)
            print('-='*60)
            sleep(1)
            print('\nVá para casa descansar, pois amanhã será um longo dia...........')
            for i in range (60):
                print('.',end='', flush=True )
                sleep(0.05)
            sleep(3)
            print()
            print('.'*60)
            
    def gameover(self):
        self.vitalidade -= 1 # Herói Perde 1 de vitalidade 
        if self.vitalidade == 0: # Se a vitalidade chegar a 0 dá Game Over
            print()
            gameover()
            print()
            exit()

class Vilao(Personagem):
    def __init__(self,clima):
        super().__init__(clima)
        ganho_forca= randint(1,5)
        self.forca += ganho_forca
        self.clima= clima
       
    def escolher_vilão(self):
        lista_viloes= ['cenouras','beterrabas','alfaces','tomates','abobrinhas','pepinos','cebolinhas','mandiocas','rabanetes','brócolis'] # lista de vilões
        lista_jaForam = list() # lista de vilões que já foram
        
        #  ZEROU O JOGO
        if lista_jaForam == lista_viloes: # se todos os vilões já tiverem saido ZEROU O JOGO!
            print("Parabéns!!!\nVocê derrotou todos os vilões e livrou a Bluefarm dos vegetais Tóxicos de uma vez por todas!!!")
            exit()
        
        # ESCOLHA DO VILÃO    
        escolha_vilao = choice(lista_viloes) #Escolhe um vilão da lista_viloes    
        while escolha_vilao in lista_jaForam:# Verifica se o vilão escolhido já está na lista_jaForam
            escolha_vilao = choice(lista_viloes) # Se estiver escolhe outro vilão

        self.nome= escolha_vilao # salvando o nome do vilão
        
        lista_jaForam.append(escolha_vilao) # adicionando vilão na lista dos que já foram
    
    def informar_dados(self):    
        # Prints dos dados do Vilão
        print('-='*60)
        sleep(0.5)
        print(f'\nOs arruaceiros da vez são {self.nome}!!!')
        sleep(1)
        print(f'{self.nome.capitalize()} têm {self.forca} pts de força.')
        
        # Influencia do clima na força do vilão
        if self.clima =='ensolarado': 
            self.forca += 3
            # Prints da mudança de força
            print()
            sleep(0.5)
            print('☀ '*45)
            sleep(0.8)
            print(f'Fez muito sol na Bluefarm e houve seca na horta dos arruaceiros.\n{self.nome.capitalize()} desviaram a irrigação dos orgânicos para si ganharam +3 de força.') 
            sleep(2)
            print(f'\n{self.nome.capitalize()} agora têm {self.forca} pts de força.')
            sleep(0.8)
            print('☀ '*45)               
        
                
# Abertura do jogo
#abertura()

# Começo do jogo
lista_clima = ['chovendo','ensolarado']
clima= choice(lista_clima)

batata= Heroi(clima)
vilao= Vilao(clima)

while True:
    print()
    print()
    if batata.clima == 'chovendo': # Começo para dias de chuva
        sleep(0.3)
        print('▬▬'*10)
        sleep(0.5)
        print('Clima: 🌨 chovendo 🌨')
        sleep(0.5)
        print('▬▬'*10)
        sleep(1)
        print(f'\nBom dia, Super Batata!')
        sleep(1)
        print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
        sleep(0.8)
        print('O que deseja fazer?')
        sleep(1)
        print('\n1- Treinar')
        sleep(0.5)
        print('2- Derrotar alguns vegetais arruaceiros')
        sleep(0.8)
        
        escolha=input('\nR:')
        while escolha not in ['1','2']:
            print('Entrada inválida!')
            sleep(1)
            print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
            sleep(1.5)
            print('Lembre-se, está chovendo!')
            sleep(1.2)
            escolha = input('R: ')
    else: # Começo para dias de sol
        sleep(0.3)
        print('▬▬'*11)
        sleep(0.5)
        print('Clima: ☀ ensolarado ☀')
        sleep(0.5)
        print('▬▬'*11)
        sleep(1)
        print(f'\nBom dia, Super Batata!')
        sleep(1)
        print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
        sleep(1.5)
        print('O que deseja fazer?')
        sleep(1)
        print('\n1- Treinar')
        sleep(1)
        print('2- Derrotar alguns vegetais arruaceiros')
        sleep(1)
        
        escolha=input('\nR:')
        while escolha not in ['1','2']:
            print('Entrada inválida!')
            sleep(1)
            print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
            sleep(1.5)
            print('Lembre-se, está ensolarado!')
            sleep(1.2)
            escolha = input('R: ')
            sleep(0.5)

    # Testando as escolhas 
    if escolha == '2': # se a escolha for enfrentar vilão
        print()
        sleep(0.5)
        print('-='*60)
        sleep(0.5)
        print('\nOs arruceiros estão plantados a mais tempo que você e se beneficiaram do uso de componentes tóxicos.\nTem certeza que deseja ataca-los?')
        sleep(1)
        print('\n1- Sim. Eu sou uma Super Batata, irei ataca-los agora mesmo!')
        sleep(1)
        print('2- Não, acho melhor treinar mais um pouquinho antes.')
        sleep(1)
        escolha= input('\nR: ')
        print()
        if escolha == '2': # se a escolha for treinar
            batata.treinar()
                
        # Se escolha for enfrentar inimigo
        if escolha== '1': 
            vilao.escolher_vilão() # escolhendo vilão
            vilao.informar_dados() # informando dados do vilão
            
            #informando dados do Herói
            print()
            sleep(1)
            print('▬▬'*19)
            sleep(1)
            print(f'\nSua força atual é: [{batata.forca} pts de força]') # print força do heroi
            sleep(0.5)
            if batata.vitalidade== 3:
                print(f'Sua vida atual é:  ███') # print vida do herói
            elif batata.vitalidade== 2:
                print(f'Sua Vida atual é:  ██')  # print vida do herói 
            elif batata.vitalidade==1:
                print(f'Sua Vida atual é :  █\n') # print vida do herói
            sleep(0.5)
            print('▬▬'*19)    
            
            # Perguntar ao usuário se deseja enfrentar:
            sleep(1)
            print('Se você perder 3 pts de vida a Bluefarm\nestará nas mãos dos vegeTóxicos!\n\nVai encarar o desafio?')
            sleep(0.5) 
            print('\n1- Bora cair pra dentro.') # 1 para sim
            sleep(0.5)
            print('2- Cê é louco cachoeira?!') # 2 para não
            sleep(0.3)
            escolha= input('\nR: ')
            print()
            sleep(0.3)
            print('-='*60)
                        
            # Batalha (Herói vs Vilão)
            if escolha =='1': # Se escolha for lutar
                if batata.forca < vilao.forca:  # se o vilão for mais forte
                    sleep(0.5)
                    print(f'Sua força atual é: [{batata.forca} pts de força]')
                    sleep(0.5)    
                    print(f'{vilao.nome.capitalize()} têm {vilao.forca} pts de força.\n')
                    sleep(1)
                    print('▬▬'*43)
                    sleep(0.5)    
                    print(f'              Você virou um purê nas mãos dos inimigos.\n              Aumente seus carboidratos e tente novamente!')
                    sleep(1)
                    print('▬▬'*43)
                    sleep(0.5)
                    print()
                    print('-='*60)
                    
                    # GAME OVER    
                    batata.gameover()

                elif batata.forca >= vilao.forca:
                    sleep(0.5)
                    print(f'\nSua força atual é: {batata.forca} pts de força')
                    sleep(0.5)
                    print(f'\n\n{vilao.nome.capitalize()}: {vilao.forca} pts de força\n')
                    sleep(1)
                    print('▬▬'*60)
                    sleep(0.5)
                    print('\n\n   Santa Batatuda...Você derrotou os inimigos!!!')
                    sleep(0.5)
                    print('   Mas, calma! A Bluefarm ainda não está livre da gange dos agroTóxicos.')
                    sleep(1)
                    print('▬▬'*60)

            elif escolha == '2':
                sleep(0.5)
                print('▬▬'*60)
                sleep(0.5)
                print(f'\nQue decepção para os Orgânicos assistir a Super Batata fugir de {vilao.nome.capitalize()}...')
                sleep(1)
                print('\nAcho melhor você deixar de ser orgulhoso e ir treinar um pouco')
                sleep(0.5)
                print('▬▬'*60)

    elif escolha == '1':
        batata.treinar()
    
    print('\nNo dia seguinte.....................................................................')    
    for i in range(80):
        print('.', end='', flush=True)
        sleep(0.05)
    print()
    # mudar o clima
    clima= choice(lista_clima)
    batata.clima=clima
    vilao.clima=clima  