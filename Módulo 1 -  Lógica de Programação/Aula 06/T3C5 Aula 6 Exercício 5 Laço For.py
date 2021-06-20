#05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
print()

from time import sleep

print('-*-*'*5)
print('Contagem Regressiva')
print('-*-*'*5)

for i in range(10,0,-1):
    print (i)
    sleep(1)

print('-*-*'*5)
print('  Feliz ano novo!!!')
print('-*-*'*5)    