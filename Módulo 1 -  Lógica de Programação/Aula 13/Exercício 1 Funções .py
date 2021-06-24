# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno

def area(largura, comprimento):
    area= largura*comprimento
    print(f'\nA área do terreno de de {area} m².' )


l=float(input('Qual a largura do terreno? '))
c=float(input('Qual o comprimento do terreno? '))

area (l,c)