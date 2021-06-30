# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class Avatar:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        if self.idade < 21:
            self.altura += (0.05 * anos)
            self.idade = idade + anos
            

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self,centímetros):
        self.altura+= centímetros/100

nome =  input('\nNome: ').title()
idade = int(input('Idade: '))
peso = float(input('Peso: ').replace(',','.'))
altura = float (input('Altura: ').replace(',','.'))
pessoa= Avatar(nome, idade,peso, altura)

acao=0
while acao!='5':
    print('\nSelecione uma opção: ')
    print('[1] Envelhecer')
    print('[2] Engordar')
    print('[3] Emagrecer')
    print('[4] Crescer')
    print('[5] Sair')
    acao= input()

    if acao == '1':
        anos= int(input('\nVai envelhecer quantos anos? '))
        pessoa.envelhecer(anos)
    elif acao == '2':
        quilos= float(input('\nVai engordar quantos quilos? '))
        pessoa.engordar(quilos)
    elif acao == '3':
        quilos= float(input('\nVai emagrecer quantos quilos? '))
        pessoa.emagrecer(quilos)    
    elif acao == '4':
        cm= float(input('\nVai crescer quantos centímetros? '))
        pessoa.crescer(cm)   


print(f'\nNome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'Peso: {pessoa.peso}Kg')
print(f'Altura: {pessoa.altura:.2f}m\n')

