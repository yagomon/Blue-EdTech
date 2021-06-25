# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
print()

def imc(p,h):
    imc= p/(h**2)
    return imc

peso= float(input('Digite seu peso: ').replace(",","."))
altura= float(input('Digite sua altura: ').replace(",","."))

print(f'\nSeu IMC é {imc(peso,altura):.2f}.\n')