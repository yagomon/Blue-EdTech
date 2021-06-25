# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas

def horaExtra(a,b):
    if b > 40:
        extra= ((b-40)*1.5)
        salárioNovo= extra+a
        return salárioNovo
    else:
        'Você não tem horas extras a receber'

print()
salario= float(input("Digite seu salário: R$ "))
htrabalho= int(input('Quantidade de horas trabalhadas: '))

print(f'\nSeu salário é R${salario}.\n\nVocê fez {htrabalho-40} hora(s) extra(s).\n\nSeu salário as com horas extras é {horaExtra(salario,htrabalho)}\n')

