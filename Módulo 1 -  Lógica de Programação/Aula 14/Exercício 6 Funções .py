# 6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F
print()

def conceito():
    nota=float(input('Digite a nota: '))

    if nota >=9.0:
        print('Conceito A')
    if nota >=8.0:
        print('Conceito B')
    if nota >=7.0:
        print('Conceito C')
    if nota >=6.0:
        print('Conceito D')
    if nota >=5.0:
        print('Conceito E')
    else:
        print('Conceito F')

conceito()                       



