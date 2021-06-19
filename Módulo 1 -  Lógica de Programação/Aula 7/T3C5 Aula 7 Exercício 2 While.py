# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.
print()

# contadores
h=0
mais18=0
f20=0

while True:
    # Entrada de idade
    age= int(input('Digite sua idade[somente números]: '))
    if age > 18: # quantidade de +18
        mais18 += 1

    #Entrade de sexo
    sex= input('\nQual seu sexo de nascimento?[M/F] ').lower()
    if sex != 'm' and sex !='f': # tratamento de entrada
        sex= input('Sexo inválido!\n Digite M para Masculino e F para Feminino: ').lower()
        
    if sex == 'f' and age < 20: # quantidade de mulheres abaixo de 20
        f20 += 1
       
    if sex == 'm': # quantidade de Homens 
        h += 1   
    # Entrada para Continuar ou Não
    proceed=input('\nDeseja inserir outra idade?[S/N] ').lower()
    if proceed != 's' and proceed != 'n': # tratamento de entrada
        proceed= input('Entrada inválida!\nDigite S para sim e N para finalizar o programa: ').lower()
        print()    
    if proceed =='n': # sair do while
        break
# testando o plural    
if h>1:
    homens='homens'
else:
    homens='homem'
if mais18>1:
    pessoas='pessoas'
else:
    pessoas='pessoa'
if f20>1:
    mulheres='mulheres'
else:
    mulheres='mulher'    

print()
print (f'{mais18} {pessoas} tem mais de 18 anos.')
print (f'{h} {homens} foram cadastrados.')         
print (f'{f20} {mulheres} tem menos de 20 anos.')

print()

Exception