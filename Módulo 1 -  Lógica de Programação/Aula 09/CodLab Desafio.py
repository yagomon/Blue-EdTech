# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
print()
print(('-=')*14)
print('GERAGOR DE NÚMEROS MEGA SENA')
print(('-=')*14)




from random import randint

jogos= int(input('\nQuantos jogos você deseja realizar? '))
cont=0
lnova= list()

while cont != jogos:  # Poderia usar 'for i in range (jogos):' e retirar o contador
    cont+=1           # economizaria 1 linha de código
    l= list()
    while len(l) != 6:
        n=randint(0,60)
        if n not in l:
            l.append(n)     
        if len(l) == 6:
            lnova.append(l)
    l=[]        

if len(lnova) >1:
    jogos='jogos'
else:
    jogos='jogo'

# print (f'\nAqui estão os números para {len(lnova)} {jogos}:\n\n{lnova}')  # imprime tudo junto [[],[],[]]

for i in range(len(lnova)):           # jogando no for vc imprime individualmente em cada linha
    print(f'\n{i+1}º jogo: {lnova[i]}')




print()
print(('-=')*14)
print('       BOA SORTE!')
print(('-=')*14)





