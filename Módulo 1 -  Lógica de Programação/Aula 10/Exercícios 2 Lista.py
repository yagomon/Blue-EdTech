# 2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista,
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o
# programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre a maior altura
# Mostre a menor altura


l=list()
maior=0
menor=100
while True:
    nome= input('\nDigite seu nome: ')
    while nome in "0123456789":
        nome= input('\nEntrada inválida.\n Entre com um nome para prosseguir: ')

    altura= input('\nDigite sua altura: ').replace(",",".")
    altura=float(altura)
    while altura not in "0123456789":
        nome= input('\nEntrada inválida.\n Digite uma altura válida para prosseguir: ')
    if altura > maior:
        maior=altura
    if altura < menor:
        menor=altura    

    l.append([nome,altura])

    proceed= input('\nDeseja continuar?[S/N] ').upper()
    while proceed not in "SN":
        proceed= input('\n Entrada inválida.\n Digite S para continuar ou N para encerrar: ').upper()
    if proceed == 'N':
        break
    
      
print()        
print(('-='*15))
print(f'{len(l)} pessoa(s) foram cadastrada(s).')    
print(f'A maior altura é {maior:.2f} e a menor é {menor:.2f}.') 
print(('-='*15))




