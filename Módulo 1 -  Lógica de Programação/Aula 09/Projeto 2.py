#### Projeto 02 – Jogo Jokenpô
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# 
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# 
# de quantidade de rodadas, se não finalize o programa.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 11.

from random import choice 

# Variáveis
l= ['pedra', 'papel','tesoura'] # lista
player= 0 # contador de vitórias do usuário
machine= 0 # contador v da máquina

# Cabeçalho
print()
print()
print(('=-')*20)
print('             J O K E N P Ô ') 
print(('=-')*20)
print()

# Ínicio do programa

while True:
    turn= str (input('Quantas partidas deseja jogar? ')) # Escolha das rodadas
    
    # Teste para entradas inválidas:
    while turn.isnumeric() != True:
        turn= str (input('\nEntrada inválida!\nDigite quantas partidas deseja jogar: [Apenas Números]: '))
    turn = int(turn)

    # Programa inteiro dentro do contador de turnos/rodadas
    for i in range (turn):
        playerchoice= input('\nVocê escolhe pedra, papel ou tesoura? ').lower() # Escolha do usuário
        
        # Teste para entradas inválidas:
        while playerchoice not in ['pedra','papel','tesoura']:
            playerchoice= input('\nEntrada inválida!\nVocê escolhe pedra, papel ou tesoura? ').lower()

        # Escolha da máquina
        machinechoice= choice(l) # Random feito com a lista l)
                    
        # Testes para ver se a Máquina venceu: 
        if machinechoice == 'pedra' and playerchoice == 'tesoura':
            machine += 1
            print(f'\nEu escolhi {machinechoice}. Você perdeu!')
        elif machinechoice == 'papel' and playerchoice == 'pedra':
            machine += 1
            print(f'\nEu escolhi {machinechoice}. Você perdeu!')
        elif machinechoice == 'tesoura' and playerchoice == 'papel':
            machine += 1
            print(f'\nEu escolhi {machinechoice}. Você perdeu!')

        # Testes para ver se o Usuário venceu:
        elif playerchoice == 'pedra' and machinechoice == 'tesoura':
            player += 1
            print(f'\nEu escolhi {machinechoice}. Você venceu!')
        elif playerchoice == 'papel' and machinechoice == 'pedra':
            player += 1
            print(f'\nEu escolhi {machinechoice}. Você venceu!')
        elif playerchoice == 'tesoura' and machinechoice == 'papel':
            player += 1
            print(f'\nEu escolhi {machinechoice}. Você venceu!')        
        # Empate:         
        else:
            print(f'\nEu escolhi {machinechoice}. Deu empate!')
                  
    
    # Cabeçalho
    print()
    print(('=-')*20)
    print('    R E S U L T A D O   G E R A L:') 
    print(('=-')*20)
    print()

    # Prints dos Resultados finais

    print(f'Você ganhou {player} partidas.\nEu ganhei {machine} partidas.\n')
    if player > machine:
        print('Parabéns!!!!!!!\nVocê é o grande campeão!!!')
    elif player < machine:
        print('Eu sou o grande campeão!')
    else:
        print('Empate!!!\nNão houve vencedores em nossa disputa.')

    print()
    print(('=-')*20)
    
    # Continuar ou sair:
    proceed= input('\nDeseja jogar novamente? ').lower()
    
    # Teste para entradas inválidas:
    while proceed not in ['sim','não']:
        proceed= input('\nEntrada inválida!\nResponda SIM se desejar jogar novamente. Caso contrário, digite NÃO: ').lower()
        
        # Encerrar
        if proceed == 'não':
            break
    break
print()           










