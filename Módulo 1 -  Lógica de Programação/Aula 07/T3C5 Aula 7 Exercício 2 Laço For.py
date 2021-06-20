## Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.
print()

num=int(input('Digite o número que deseja saber a tabuada: '))

print()

for i in range (10):
    print(f'{num} x {i+1} = {num*(i+1)}')
     
