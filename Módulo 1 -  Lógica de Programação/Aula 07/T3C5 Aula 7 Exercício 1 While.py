#### Crie um programa que leia dois valores e mostre um menu na tela:
#### [ 1 ] somar
#### [ 2 ] multiplicar
#### [ 3 ] maior
#### [ 4 ] novos números
#### [ 5 ] sair do programa
#### Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)
print()

n1= float(input('Digite um valor para realizar uma operação lógica ou matemática: ').replace(',' , '.'))
n2= float(input('Digite o segundo valor para realizar uma operação lógica ou matemática: ').replace(',' , '.'))

print()

menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()

if menu == '1':
    menu='somar'
if menu == '2':
    menu='multiplicar'
if menu == '3':
    menu='maior'
if menu == '4':
    menu='novos números'
if menu == '5':
    menu='sair do programa'



while menu != 'sair do programa':
    if menu=='somar':
        print(f' A soma de {n1} + {n2} é {n1+n2}')
        menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()

    if menu=='multiplicar':
        print(f'A multiplicação de {n1} + {n2} é {n1*n2}')
        menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()

    if menu=='maior':
        if n1>n2 == True:
            print(f'o número {n1} é maior que o {n2}.')
            menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()
        else:
            print(f'o número {n1} não é maior que o {n2}.')
            menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()


    if menu=='novos números':
        
        n1= float(input('Digite um valor para realizar uma operação lógica ou matemática: ').replace(',' , '.'))
        
        n2= float(input('Digite o segundo valor para realizar uma operação lógica ou matemática: ').replace(',' , '.'))

        print()

        menu= input('Qual opereção deseja realizar?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n').lower()
        
    
print()

print('Programa finalizado')
