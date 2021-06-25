# 7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
print()

def compara(a,b):
    if a<b:
        print(f'{a} é menor que {b}.')
    elif a>b:
        print(f'{b} é menor que {a}.')
    else:
        print(f'{b} e {a} são iguais.')

n1= int(input('Digite um número: '))
n2= int(input('Digite outro número: '))
print()

compara(n1,n2)