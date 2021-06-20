#2 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores.

print()
n= int (input('Digite um número para descubrir todos os seus divisores: '))
print()

for i in range (1,n):
    div= n/i
    if n%i == 0:
        print(f'O número {div:.0f} é divisor de {n}.')

print()