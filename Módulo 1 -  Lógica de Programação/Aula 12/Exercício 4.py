# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar

d=dict()

name= input('\nDigite seu nome: ')
birthyear= int(input("Digite sua data de nascimento: "))
ctps= int(input("Digite o nº da Carteira de Trabalho: "))

d['name']= name
d['birthyear']= birthyear
d['ctps']= ctps



if d['ctps'] != 0:
    contratacao= int(input("Digite o ano de contratação do seu primeiro emprego: "))
    salario=float(input('Digite o salário: R$').replace(',','.'))
else:
    print('Informações insuficientes para o cálculo da aposentadoria!')  

d['contratação']= contratacao
d['salário']= salario

aposentadoria= (d['contratação'] + 35) - birthyear

print()
print(d['name'],f'irá se apodentar com {aposentadoria} anos.')







    