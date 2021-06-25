
# 1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a,b,c):
    soma= a+b+c
    return soma

arg1= int(input("Digite um número: "))
arg2= int(input("Digite outro número: "))
arg3= int(input("Digite outro número: "))

print(f'A soma de {arg1}, {arg2}, {arg3} é {soma(arg1,arg2,arg3)}.')