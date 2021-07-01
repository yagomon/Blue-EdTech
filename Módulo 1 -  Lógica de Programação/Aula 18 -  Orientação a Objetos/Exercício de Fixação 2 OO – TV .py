# Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Tv:
    def __init__(self):
        self.canal= 4
        self.volume=10

    def escolherCanal(self, canal):
        while canal.isnumeric() ==False:
            canal=input('Entrada inválida!\n\nDigite um número entre 1 e 100 para selecionar um canal válido.\n')
        canal= int(canal)
        
        while 0>canal>100:
            canal=input('Entrada inválida!\n\nDigite um número entre 1 e 100 para selecionar um canal válido.\n')
        self.canal=canal


    def aumentarVolume(self):
        if self.volume< 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume> 0:
            self.volume -= 1

    def getStatus(self):
        print()
        print('-='*15)
        print('   S t a t u s   d a   T V'.upper())
        print('--'*15)
        print(f'\nCanal: {self.canal}.')
        print(f'Volume: {self.volume}.\n')
        print('-='*15)

tv= Tv()

print('\nBem-vindo a Python Tv!\n\nDigite o número da opção desejada:\n')
print('1- Escolher canal.')
print('2- Aumentar volume.')
print('3- Diminuir volume')
acao= input('opção: ')
while acao.isnumeric()!=True:
    acao= input('Entrada Inválida\n\nEscolha [1] para muda o canal, [2] para aumentar ou [3] para diminuir o volume: ')
acao = int(acao)    


if acao == 1:
    canal=input('\nDigite o número do canal desejado:\ncanal: ')
    tv.escolherCanal(canal)    
    
elif acao == 2:
    tv.aumentarVolume()

if acao == 3:
    tv.diminuirVolume()

continuar= input('\nDeseja realizar outra ação? [S/N]\nR:').upper()

while continuar =='S':
    acao= input('\nEscolha a ação que deseja realizar:\n1- Trocar canal\n2- Aumentar volume\n3- Diminuir volume\nopção: ')

    while acao.isnumeric()!=True:
        acao= input('Entrada Inválida\n\nEscolha [1] para muda o canal, [2] para aumentar ou [3] para diminuir o volume: ')
    acao = int(acao)    

    if acao == 1:
        canal=input('\nDigite o número do canal desejado:\ncanal ')
        tv.escolherCanal(canal)    
    elif acao == 2:
        tv.aumentarVolume()
    if acao == 3:
        tv.diminuirVolume()

    continuar= input('Deseja realizar outra ação? [S/N]').upper()


tv.getStatus()    
