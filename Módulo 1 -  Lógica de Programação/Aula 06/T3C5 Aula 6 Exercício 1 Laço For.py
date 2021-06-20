###1 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparecem as vogais a,e,i,o,u.

f= input('\nDigite uma frase: ')

vogais= 0

for i in f:
    if i in "aeiouáàâéêíóôAEIOUÁÀÂÉÊÍÓÔ":
        vogais+= 1

print(f'\nA frase "{f}" tem {vogais} vogais.')
print()