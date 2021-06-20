##Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
print()

maior=0
menor=0

for i in range(7):
    ano= int(input(f'Em que a {i+1}ª pessoa nasceu? '))
    idade= 2021-ano
    if idade<18:
        menor+=1
    else:
        maior+=1

if maior>1:
    verbo="são maiores"
else:
    verbo="é maior"

if menor>1:
    pessoas="pessoas"
else:
    pessoas="pessoa"    

print (f'{menor} {pessoas} ainda não atingiram a maioridade e {maior} já {verbo}.')

