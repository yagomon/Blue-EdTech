# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.

def testeNumeroNota (n,aluno):
    # Testa se a string é um numero e retorna um input
    while n.isnumeric()!= True:
        n = input(f'Entrada inválida!\n\nDigite nota de {aluno} [SOMENTE NÚMEROS]: ')
        print()



d=dict()
l=list()



for cont in range (2):
    aluno = input('\nDigite o nome do aluno(a): ')
    n1 = input(f'1ª nota de {aluno}: ')
    testeNumeroNota(n1,aluno)
    n2 = input(f'2ª nota de {aluno}: ')
    testeNumeroNota(n2,aluno)
    n3 = input(f'3ª nota de {aluno}: ')
    testeNumeroNota(n3,aluno)
    n4 = input(f'4ª nota de {aluno}: ')
    testeNumeroNota(n4,aluno)
    n5 = input(f'5ª nota de {aluno}: ')
    testeNumeroNota(n5,aluno)

    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
    n4=float(n4)
    n5=float(n5)

    media= (n1+n2+n3+n4+n5)/5

    d['nome']=aluno
    d['n1']= n1
    d['n2']= n2
    d['n3']= n3
    d['n4']= n4
    d['n5']= n5
    d['média']= media
           
    if media >= 7:
        d['situação']='aprovado!'
    elif media < 6.9 and media >= 5:
        d['situação']='recuperação!'
    else:
        d['situação']= 'reprovado!'

    l.append(d)
    d={}    

for i in l:
    print(f"\n{i['nome']} {i['situação']}!\n{i['nome']} tirou {i['n1']}, {i['n2']}, {i['n3']}, {i['n4']}, {i['n5']} ficando com média {i['média']}.\n")     