# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

d=dict()

aluno = input('Digite o nome do aluno: ')
media = float(input(f'Digite a media de {aluno}: '))

d[aluno] = media

if d[aluno] >= 7:
    print('Você foi aprovado!')
elif d[aluno] < 6.9 and d[aluno] >= 5:
    print('Você esta de recuperação!')
else:
    print('Você foi reprovado!')
