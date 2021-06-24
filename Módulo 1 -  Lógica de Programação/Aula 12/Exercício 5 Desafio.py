# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

lista=list()
d=dict()
listaMulheres=[]

while True:
    nome= input('\nDigite seu nome: ').capitalize()
    
    sexo= input("Digite seu sexo biológico[M/F]: ").upper()
    while sexo != ['F','M']:
        sexo= input("Entrada inválida!\n\nDigite F para feminino e M para masculino: ").upper()
    
    idade= input('Digite sua idade: ')
    while idade.isnumeric != True :
        idade= input('"Entrada inválida!\n\nDigite sua idade [APENA NÚMEROS]: ')
    idade=int(idade)     
    
    d['nome']= nome
    d['sexo']= sexo
    d['idade']= idade
    lista.append(d)
    d={}

    proceed=input('Deseja fazer outro cadastro?[S/N] ').upper()

    while proceed not in ['S','N']:
        proceed=input('Entrada inválida!\n\nDigite S para sim ou N para não: ').upper()
    if proceed == 'N':
        break
    
somaIdade=0
for i in lista:
    somaIdade += i['idade']
    
for i in lista:
    if i['sexo']=='F':
        listaMulheres.append(i)   

print(f'\n{len(lista)} pessoas foram cadastradas!')

print(f'Soma das idades: {somaIdade}.')

print(f'Informações das mulheres cadastradas:\n {listaMulheres}.')

