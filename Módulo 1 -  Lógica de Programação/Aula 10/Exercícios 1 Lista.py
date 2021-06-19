# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

l=list()
for i in range (5):
    nome= input('Digite seu nome: ')
    idade= int(input('Digite sua idade: '))

    
    l.append([nome,idade])

for i in range (5):    
    if l[i][1] > 18 :
        print(f'{l[i][0]} é maior de idade.')
    else:
        print(f'{l[i][0]} é menor de idade.')    

