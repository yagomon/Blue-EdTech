###Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.Mostre também quantos valores pares foram digitados.

print()

par = 0

for i in range(6):
    n=int(input('Digite um número: '))
    if n%2 == 0:
        par +=1